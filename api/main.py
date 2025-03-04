from fastapi import FastAPI, Response
from fastapi.responses import StreamingResponse
import os
from random import randint
from functools import lru_cache
from typing import Dict, Tuple, Optional
import hashlib
import time

# Vercel環境でのみ動作か判定
is_vercel = os.environ.get('VERCEL') == '1'

# Vercel環境でのみ動作
if is_vercel:
    from api import hoyo_api
    from api import img
else:
    import hoyo_api
    import img

app = FastAPI()

# メモリキャッシュの実装
_card_cache: Dict[str, Tuple[bytes, float]] = {}
CACHE_DURATION = 1800  # 30分のキャッシュ

def _get_cache_key(uid: int, lang: str, top: str, bottom: str, hide_uid: bool, bg: int) -> str:
    """キャッシュキーの生成"""
    key = f"{uid}_{lang}_{top}_{bottom}_{hide_uid}_{bg}"
    return hashlib.md5(key.encode()).hexdigest()

# Vercel環境でのパス解決
def get_asset_path(path: str) -> str:
    if is_vercel:
        return os.path.join(os.getcwd(), path)
    return path

@app.get("/api/info")
def index():
    return {"message": "API is Run!"}

@app.get("/api/card/gi")
async def get_image(uid: int, lang: str="en",
                    top: str="left", bottom: str="right",
                    hide_uid: bool=False, bg: Optional[int]=None):
    # キャッシュキーの生成
    cache_key = _get_cache_key(uid, lang, top, bottom, hide_uid, bg)
    current_time = time.time()

    # キャッシュチェック
    if cache_key in _card_cache:
        cached_data, cache_time = _card_cache[cache_key]
        if current_time - cache_time < CACHE_DURATION:
            return Response(content=cached_data, media_type="image/png")

    # 初期設定
    font = get_asset_path("assets/fonts/gi.ttf")
    localization = img.load_localization(lang)
    
    # 背景画像の設定
    if bg is None:
        # 画像ファイルのリストを取得
        img_dir = get_asset_path("assets/img/gi")
        files = os.listdir(img_dir)
        image_files = [f.split('.')[0] for f in files if f.endswith(('.png', '.jpg', '.jpeg', '.webp'))]
        if image_files:
            bg_id = randint(1, len(image_files))
        else:
            bg_id = 1  # デフォルト値
    else:
        bg_id = bg

    # ベース画像の作成
    base_img_path = get_asset_path(f"assets/img/gi/{bg_id}.png")
    gradient_path = get_asset_path("assets/img/gradient.png")
    im = img.create_base_image(base_img_path, gradient_path)

    # ユーザー情報の取得
    hoyo_user_data = await hoyo_api.fetch_user_data(uid)

    if not hoyo_user_data:
        return {"error": "Failed to fetch user data"}

    # ユーザー情報の整形（hoyo_api.UserInfo から img.UserInfo への変換）
    user_info = img.convert_hoyo_to_img_userinfo(hoyo_user_data, uid, lang, localization)
    user_info.hide_uid = hide_uid  # hide_uidの設定を反映

    # 画像の描画
    im = img.draw_user_info(im, user_info, top, bottom, font, localization)
    
    # 画像をbyteに変換
    from io import BytesIO
    img_byte_arr = BytesIO()
    im.save(img_byte_arr, format='PNG', optimize=True)
    img_byte_arr.seek(0)
    
    # キャッシュの保存
    _card_cache[cache_key] = (img_byte_arr.getvalue(), current_time)
    
    return StreamingResponse(img_byte_arr, media_type="image/png")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, port=8000)
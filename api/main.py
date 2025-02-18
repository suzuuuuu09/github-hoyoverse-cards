from fastapi import FastAPI
from fastapi.responses import StreamingResponse
import os
from random import randint

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

@app.get("/api")
def index():
    return {"message": "API is Run!"}

@app.get("/api/card")
async def get_image(uid: int, lang: str="en",
                    top: str="left", bottom: str="right",
                    hide_uid: bool=False, bg: int=None):
    # 初期設定
    font = "assets/fonts/gi.ttf"
    localization = img.load_localization(lang)
    
    # 背景画像の設定
    if bg is None:
        # 画像ファイルのリストを取得
        files = os.listdir("assets/img/gi")
        image_files = [f for f in files if f.endswith(('.png', '.jpg', '.jpeg', '.webp'))]
        bg_id = randint(1, len(image_files))
    else:
        bg_id = bg

    # ベース画像の作成
    im = img.create_base_image(f"assets/img/gi/{bg_id}.png", "assets/img/gradient.png")

    # ユーザー情報の取得
    hoyo_user_data = await hoyo_api.fetch_user_data(uid)

    if not hoyo_user_data:
        return {"error": "Failed to fetch user data"}

    # ユーザー情報の整形（hoyo_api.UserInfo から img.UserInfo への変換）
    user_info = img.UserInfo(
        name=hoyo_user_data.user_name,
        adventure_rank=hoyo_user_data.adventure_rank,
        achievement=str(hoyo_user_data.achievement or "-"),
        friendship_max=str(hoyo_user_data.friendship_max or "-"),
        tower=f"{hoyo_user_data.tower.floor or ''}-{hoyo_user_data.tower.level or ''}" if hoyo_user_data.tower else "-",
        theater=localization['theater_act'].format(act=hoyo_user_data.theater.act) if hoyo_user_data.theater and hoyo_user_data.theater.act else "-",
        uid=uid,
        hide_uid=hide_uid
    )

    # 画像の描画
    im = img.draw_user_info(im, user_info, top, bottom, font, localization)
    
    # 画像をbyteに変換
    from io import BytesIO
    img_byte_arr = BytesIO()
    im.save(img_byte_arr, format='PNG')
    img_byte_arr.seek(0)

    return StreamingResponse(img_byte_arr, media_type="image/png")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, port=8000)
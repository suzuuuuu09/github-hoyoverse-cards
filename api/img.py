from PIL import Image, ImageDraw, ImageFont, ImageChops
from dataclasses import dataclass
from typing import Tuple, TYPE_CHECKING, Dict
from functools import lru_cache
import json
if TYPE_CHECKING:
    from PIL.Image import Image
import asyncio
import os

# Vercel環境でのみ動作か判定
is_vercel = os.environ.get('VERCEL') == '1'

# Vercel環境でのみ動作
if is_vercel:
    from api import hoyo_api
else:
    import hoyo_api

@dataclass
class TextPosition:
    x: int
    y: int
    text: str
    font_size: int
    color: str = "#fcfcfc"

@dataclass
class UserInfo:
    name: str
    adventure_rank: int
    achievement: str
    friendship_max: str
    tower: str
    theater: str
    uid: int
    hide_uid: bool = False

def get_asset_path(path: str) -> str:
    """Vercel環境でのパス解決"""
    if is_vercel:
        return os.path.join(os.getcwd(), path)
    return path

def text_image(path, text):
    """テキストを画像に描画"""
    im = Image.open(get_asset_path(path))
    draw = ImageDraw.Draw(im)
    font = ImageFont.truetype(get_asset_path("assets/fonts/gi.ttf"), 36)
    draw.text((10, 10), text=text, font=font, fill=(0, 0, 0))
    return im

@lru_cache(maxsize=128)
def get_font(font_path: str, size: int) -> ImageFont.FreeTypeFont:
    """フォントをキャッシュして返す"""
    return ImageFont.truetype(get_asset_path(font_path), size)

def draw_text_image(im: Image, text: str, location: Tuple[int, int], font_path: str, font_size: int, color: str = "#fcfcfc") -> Image:
    """テキストを画像に挿入（最適化版）"""
    draw = ImageDraw.Draw(im)
    font = get_font(font_path, font_size)
    draw.text(location, text=text, font=font, fill=color)
    return im

@lru_cache(maxsize=128)
def get_text_width(text: str, font_path: str, font_size: int) -> int:
    """テキストの幅を取得（キャッシュ付き）"""
    font = get_font(font_path, font_size)
    bbox = font.getbbox(text)
    return bbox[2] - bbox[0]

@lru_cache(maxsize=128)
def get_text_height(text: str, font_path: str, font_size: int) -> int:
    """テキストの高さを取得（キャッシュ付き）"""
    font = get_font(font_path, font_size)
    bbox = font.getbbox(text)
    return bbox[3] - bbox[1]

def crop_center_image(im: Image, crop_w: int, crop_h: int) -> Image:
    """画像を中心で切り抜き"""
    im_w, im_h = im.size
    im_crop = im.crop((
        (im_w - crop_w) // 2,
        (im_h - crop_h) // 2 - 200,  # NOTE:キャラの顔が写ってないことが多かったから200px下げた
        (im_w + crop_w) // 2,
        (im_h + crop_h) // 2 - 200
    ))
    return im_crop

def smart_crop_image(im: Image, target_w: int, target_h: int) -> Image:
    """
    画像を賢く切り抜き、指定サイズにリサイズする
    
    Args:
        im (Image): 入力画像
        target_w (int): 目標の幅
        target_h (int): 目標の高さ
        
    Returns:
        Image: 処理後の画像
    """
    # 元画像のサイズを取得
    im_w, im_h = im.size
    target_ratio = target_w / target_h
    
    # Step 1: アスペクト比の調整
    if im_w / im_h > target_ratio:
        # 画像が横長すぎる場合
        new_w = int(im_h * target_ratio)
        crop_x = (im_w - new_w) // 2
        im = im.crop((crop_x, 0, crop_x + new_w, im_h))
    elif im_w / im_h < target_ratio:
        # 画像が縦長すぎる場合
        new_h = int(im_w / target_ratio)
        crop_y = (im_h - new_h) // 2
        im = im.crop((0, crop_y, im_w, crop_y + new_h))
    
    # Step 2: リサイズ
    im = im.resize((target_w, target_h), Image.Resampling.LANCZOS)
    
    return im

def multiply_image(base_im, overlay_im, opacity: float):
    """画像の乗算"""
    base_im = base_im.convert("RGBA")
    overlay_im = overlay_im.convert("RGBA")
    im_multiplied = ImageChops.multiply(base_im, overlay_im)
    im = Image.blend(base_im, im_multiplied, opacity)
    return im

@lru_cache(maxsize=1)
def load_localization(lang: str = "en") -> dict:
    """言語設定ファイルを読み込む（キャッシュ付き）"""
    file_path = get_asset_path("assets/localization.json")
    with open(file_path, "r", encoding="utf-8") as f:
        return json.load(f)[lang]

_image_cache: Dict[str, Image.Image] = {}

def create_base_image(base_path: str, overlay_path: str, opacity: float = 0.7) -> Image:
    """ベース画像の作成（キャッシュ付き）"""
    cache_key = f"{base_path}_{overlay_path}_{opacity}"
    if cache_key in _image_cache:
        return _image_cache[cache_key].copy()

    base_im = Image.open(get_asset_path(base_path))
    overlay_im = Image.open(get_asset_path(overlay_path))
    result = multiply_image(base_im, overlay_im, opacity)
    _image_cache[cache_key] = result
    return result.copy()

def calculate_text_position(align: str, image_width: int, total_width: int, margin: int = 10) -> int:
    """テキストの開始位置を計算"""
    match align:
        case "left":
            return margin
        case "center":
            return (image_width - total_width) // 2
        case "right":
            return image_width - total_width - margin

def draw_text_group(im: Image, position: TextPosition, font_path: str) -> Image:
    """テキストグループを描画"""
    return draw_text_image(
        im=im,
        location=(position.x, position.y),
        text=position.text,
        font_path=font_path,
        font_size=position.font_size,
        color=position.color
    )

def draw_stats_item(im: Image, start_x: int, label: str, value: str, font_path: str,
                    item_spacing: int, localization: dict) -> Tuple[Image, int]:
    """統計項目を描画"""
    # ラベルの描画
    im = draw_text_image(
        im=im,
        location=(start_x, 160),
        text=localization[label],
        font_path=font_path,
        font_size=12,
        color="#d0d0d0"
    )

    # ラベルの幅を取得
    text_width = get_text_width(localization[label], font_path, 12)

    # 値の描画
    im = draw_text_image(
        im=im,
        location=(start_x + (text_width - get_text_width(str(value), font_path, 16)) / 2, 140),
        text=str(value),
        font_path=font_path,
        font_size=16
    )

    return im, text_width

def draw_user_info(im: Image, user_info: UserInfo, align_top: str, align_bottom: str,
                   font_path: str, localization: dict) -> Image:
    """ユーザー情報を描画"""
    image_width = im.size[0]

    # 上部の配置計算
    name_width = get_text_width(user_info.name, font_path, 16)
    rank_width = get_text_width(f"Lv. {user_info.adventure_rank}", font_path, 10)
    uid_width = get_text_width(f"UID: {user_info.uid}", font_path, 12)
    top_total_width = name_width + rank_width + 5

    name_start_x = calculate_text_position(align_top, image_width, top_total_width)
    uid_start_x = calculate_text_position(align_top, image_width, uid_width)

    # 上部の描画
    positions = [
        TextPosition(x=name_start_x, y=10, text=user_info.name, font_size=16),
        TextPosition(x=name_start_x + name_width + 5, y=15, text=f"Lv. {user_info.adventure_rank}", font_size=10),
    ]

    # UIDを隠さない場合のみUIDを追加
    if not user_info.hide_uid:
        uid_width = get_text_width(f"UID: {user_info.uid}", font_path, 12)
        uid_start_x = calculate_text_position(align_top, image_width, uid_width)
        positions.append(
            TextPosition(x=uid_start_x, y=30, text=f"UID: {user_info.uid}", font_size=12)
        )

    for pos in positions:
        im = draw_text_group(im, pos, font_path)

    # 下部の統計情報の描画
    item_spacing = 10
    start_x = calculate_text_position(align_bottom, image_width, bottom_total_width(localization, font_path, item_spacing))

    stats = [
        ("achievements", user_info.achievement),
        ("max_friendship", user_info.friendship_max),
        ("spiral_abyss", user_info.tower),
        ("imaginarium_theater", user_info.theater)
    ]

    current_x = start_x
    for label, value in stats:
        im, width = draw_stats_item(im, current_x, label, value, font_path, item_spacing, localization)
        current_x += width + item_spacing

    return im

def bottom_total_width(localization: dict, font_path: str, item_spacing: int) -> int:
    """下部の全体幅を計算"""
    labels = ['achievements', 'max_friendship', 'spiral_abyss', 'imaginarium_theater']
    widths = [get_text_width(localization[label], font_path, 12) for label in labels]
    return sum(widths) + item_spacing * 3

def add_rounded_corners(im: Image, radius: int) -> Image:
    """
    画像に角丸を適用する
    
    Args:
        im (Image): 入力画像
        radius (int): 角の半径（ピクセル）
        
    Returns:
        Image: 角丸処理後の画像
    """
    # アルファチャンネル付きの新しい画像を作成
    circle = Image.new('L', (radius * 2, radius * 2), 0)
    draw = ImageDraw.Draw(circle)
    draw.ellipse((0, 0, radius * 2 - 1, radius * 2 - 1), fill=255)
    
    # アルファチャンネル用のマスクを作成
    alpha = Image.new('L', im.size, 255)
    w, h = im.size
    
    # 四隅にマスクを適用
    alpha.paste(circle.crop((0, 0, radius, radius)), (0, 0))  # 左上
    alpha.paste(circle.crop((radius, 0, radius * 2, radius)), (w - radius, 0))  # 右上
    alpha.paste(circle.crop((0, radius, radius, radius * 2)), (0, h - radius))  # 左下
    alpha.paste(circle.crop((radius, radius, radius * 2, radius * 2)), (w - radius, h - radius))  # 右下
    
    # 画像をRGBAモードに変換し、マスクを適用
    im = im.convert('RGBA')
    im.putalpha(alpha)
    
    return im

def convert_hoyo_to_img_userinfo(hoyo_user: 'hoyo_api.UserInfo', uid: int, lang: str, localization: dict) -> UserInfo:
    """
    hoyo_apiのUserInfoをimg用のUserInfoに変換する
    """
    return UserInfo(
        name=hoyo_user.user_name,
        adventure_rank=hoyo_user.adventure_rank,
        achievement=str(hoyo_user.achievement or "-"),
        friendship_max=str(hoyo_user.friendship_max or "-"),
        tower=f"{hoyo_user.tower.floor or '-'}-{hoyo_user.tower.level or '-'}" if hoyo_user.tower else "-",
        theater=localization['theater_act'].format(act=hoyo_user.theater.act) if hoyo_user.theater and hoyo_user.theater.act else "-",
        uid=uid,
        hide_uid=False
    )

if __name__ == "__main__":
    try:
        # 初期設定
        font = get_asset_path("assets/fonts/gi.ttf")
        localization = load_localization("jp")  # 日本語を指定

        # ベース画像の作成
        im = create_base_image(get_asset_path("assets/img/gi/1.png"), get_asset_path("assets/img/gradient.png"))

        # ユーザー情報の取得
        uid = 801081402
        user_data = asyncio.run(hoyo_api.fetch_user_data(uid))
        
        if user_data is None:
            print("ユーザー情報の取得に失敗しました")
            exit(1)

        # UserInfoの変換
        user_info = convert_hoyo_to_img_userinfo(user_data, uid, "jp", localization)

        # 画像の描画
        im = draw_user_info(im, user_info, "left", "right", font, localization)

        # 角丸を適用
        im = add_rounded_corners(im, 20)

        # 画像の保存
        output_path = get_asset_path("assets/img/preview.png")
        im.save(output_path)
        print(f"画像を保存しました: {output_path}")

    except Exception as e:
        print(f"エラーが発生しました: {e}")

from PIL import Image, ImageDraw, ImageFont, ImageChops
import base64
from io import BytesIO
import hoyo_api
import asyncio
import json


def text_image(path, text):
    im = Image.open(path)

    draw = ImageDraw.Draw(im)
    font = ImageFont.truetype("assets/fonts/gi.ttf", 36)
    draw.text((10, 10), text=text, font=font, fill=(0, 0, 0))

    # buffered = BytesIO()
    # im.save(buffered, format="PNG")
    # buffered.seek(0)
    # return buffered
    return im

def draw_text_image(im, text, location, font, font_size, color="#fcfcfc"):
    draw = ImageDraw.Draw(im)
    font = ImageFont.truetype(font, font_size)
    draw.text(location, text=text, font=font, fill=color)
    return im

def get_text_width(text, font, font_size):
    """テキストの幅を取得"""
    font = ImageFont.truetype(font, font_size)
    bbox = font.getbbox(text)
    return bbox[2] - bbox[0]

def get_text_height(text, font, font_size):
    """テキストの高さを取得"""
    font = ImageFont.truetype(font, font_size)
    bbox = font.getbbox(text)
    return bbox[3] - bbox[1]

def crop_center_image(crop_w, crop_h):
    """画像を中心で切り抜き"""
    im = Image.open("assets/img/gi/0.png")
    im_w, im_h = im.size
    im_crop = im.crop((
        (im_w - crop_w) // 2,
        (im_h - crop_h) // 2 - 200,  # NOTE:キャラの顔が写ってないことが多かったから200px下げた
        (im_w + crop_w) // 2,
        (im_h + crop_h) // 2 - 200
    ))
    return im_crop

def multiply_image(base_im, overlay_im, opacity: float):
    """画像の乗算"""
    base_im = base_im.convert("RGBA")
    overlay_im = overlay_im.convert("RGBA")
    im_multiplied = ImageChops.multiply(base_im, overlay_im)
    im = Image.blend(base_im, im_multiplied, opacity)
    return im

if __name__ == "__main__":
    # im = crop_center_image(2100, 756)

    # NOTE: 500x180のサイズにしたのはGithub上で都合がよかったサイズ
    # im.resize((500, 180)).save("assets/img/gi/rs_0.png")
    base_im = Image.open("assets/img/gi/rs_0.png")
    overlay_im = Image.open("assets/img/gradient.png")
    im = multiply_image(base_im, overlay_im, 0.8)
    font = "assets/fonts/gi.ttf"


    # 言語設定ファイルの読み込み
    with open("assets/localization.json", "r", encoding="utf-8") as f:
        localization = json.load(f)
    lang = "ja"

    uid = 801081402
    user_info = asyncio.run(hoyo_api.fetch_user_data(uid))

    user_name = user_info["user_name"]  # ユーザー名
    adv_rank = "Lv." + str(user_info["adventure_rank"])  # 冒険ランク
    achv = str(user_info.get("achievement", "-"))  # アチーブメント数
    max_friendship = user_info.get("friendship_max", "-")  #  好感度MAXキャラ数
    tower = f"{user_info['tower'].get('floor', '-')}-{user_info['tower'].get('level', '-')}" if user_info.get('tower') else "-"  # 螺旋
    theater = localization[lang]['theater_act'].format(act=user_info['theater']['act']) if user_info.get('theater', {}).get('act') else "-"  # 幻想シアター

    align_top = "left"
    align_bottom = "right"
    image_width = base_im.size[0]

    # 上部の合計幅を計算
    name_width = get_text_width(user_name, font, 16)
    rank_width = get_text_width(adv_rank, font, 10)
    uid_width = get_text_width(f"UID: {str(uid)}", font, 12)
    top_total_width = name_width + rank_width + 5  # 名前とランクの間のスペース

    # 上部の開始位置を計算
    match align_top:
        case "left":
            name_start_x = 10
            uid_start_x = 10
        case "center":
            name_start_x = (image_width - top_total_width) // 2
            uid_start_x = (image_width - uid_width) // 2  # UIDを中央揃え
        case "right":
            name_start_x = image_width - top_total_width - 10
            uid_start_x = image_width - uid_width - 10  # UIDを右揃え

    # 名前の挿入
    im = draw_text_image(
        im=im,
        location=(name_start_x, 10),
        text=user_name,
        font=font,
        font_size=16
    )

    # 冒険ランクの挿入
    im = draw_text_image(
        im=im,
        location=(name_start_x + name_width + 5, 15),
        text=adv_rank,
        font=font,
        font_size=10
    )

    # UIDの挿入
    im = draw_text_image(
        im=im,
        location=(uid_start_x, 30),
        text=f"UID: {str(uid)}",
        font=font,
        font_size=12
    )

    item_spacing = 10  # 項目間のスペース
    bottom_total_width = (
        get_text_width(localization[lang]["achievements"], font, 12) +
        get_text_width(localization[lang]["max_friendship"], font, 12) +
        get_text_width(localization[lang]["spiral_abyss"], font, 12) +
        get_text_width(localization[lang]["imaginarium_theater"], font, 12) +
        item_spacing * 3  # 項目間のスペース
    )

    match align_bottom:
        case "left":
            start_bottom_x = 10
        case "center":
            start_bottom_x = (image_width - bottom_total_width) // 2
        case "right":
            start_bottom_x = image_width - bottom_total_width - 10

    # アチーブメント数の挿入
    im = draw_text_image(
        im=im,
        location=(start_bottom_x, 160),
        text=localization[lang]["achievements"],
        font=font,
        font_size=12,
        color="#a0a0a0"
    )
    achv_text_width = get_text_width(localization[lang]["achievements"], font, 12)
    im = draw_text_image(
        im=im,
        location=(start_bottom_x + (achv_text_width - get_text_width(achv, font, 16)) / 2, 140),
        text=f"{achv}",
        font=font,
        font_size=16
    )

    # 好感度MAXキャラ数の挿入
    friendship_start_x = start_bottom_x + achv_text_width + item_spacing
    im = draw_text_image(
        im=im,
        location=(friendship_start_x, 160),
        text=localization[lang]["max_friendship"],
        font=font,
        font_size=12,
        color="#a0a0a0"
    )
    max_friendship_text_width = get_text_width(localization[lang]["max_friendship"], font, 12)
    im = draw_text_image(
        im=im,
        location=(friendship_start_x + (max_friendship_text_width - get_text_width(str(max_friendship), font, 16)) / 2, 140),
        text=f"{max_friendship}",
        font=font,
        font_size=16
    )

    # 螺旋の挿入
    spiral_start_x = friendship_start_x + max_friendship_text_width + item_spacing
    im = draw_text_image(
        im=im,
        location=(spiral_start_x, 160),
        text=localization[lang]["spiral_abyss"],
        font=font,
        font_size=12,
        color="#a0a0a0"
    )
    tower_text_width = get_text_width(localization[lang]["spiral_abyss"], font, 12)
    im = draw_text_image(
        im=im,
        location=(spiral_start_x + (tower_text_width - get_text_width(tower, font, 16)) / 2, 140),
        text=f"{tower}",
        font=font,
        font_size=16
    )

    # 幻想シアターの挿入
    theater_start_x = spiral_start_x + tower_text_width + item_spacing
    im = draw_text_image(
        im=im,
        location=(theater_start_x, 160),
        text=localization[lang]["imaginarium_theater"],
        font=font,
        font_size=12,
        color="#a0a0a0"
    )
    theater_text_width = get_text_width(localization[lang]["imaginarium_theater"], font, 12)
    im = draw_text_image(
        im=im,
        location=(theater_start_x + (theater_text_width - get_text_width(theater, font, 16)) / 2, 140),
        text=theater,
        font=font,
        font_size=16
    )

    im.save("assets/img/gi/preview.png")

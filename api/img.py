from PIL import Image, ImageDraw, ImageFont, ImageChops
import base64
from io import BytesIO

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

def draw_text_image(im, text, font, font_size):
    draw = ImageDraw.Draw(im)
    font = ImageFont.truetype(font, font_size)
    draw.text((10, 10), text=text, font=font, fill=(252, 252, 252))
    return im

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

def multiply_image(base_im, overlay_im, opacity:float):
    """画像の乗算"""
    base_im = base_im.convert("RGBA")
    overlay_im = overlay_im.convert("RGBA")
    im_multiplied = ImageChops.multiply(base_im, overlay_im)
    im = Image.blend(base_im, im_multiplied, opacity)
    return im

if __name__ == "__main__":
    # im = crop_center_image(2100, 756)

    # NOTE: 500x180のサイズにしたのはGithub上でちょうどいいサイズ
    # im.resize((500, 180)).save("assets/img/gi/rs_0.png")
    base_im = Image.open("assets/img/gi/rs_0.png")
    overlay_im = Image.open("assets/img/gradient.png")
    im = multiply_image(base_im, overlay_im, 0.8)
    text = "うほう"
    font = "assets/fonts/gi.ttf"
    im = draw_text_image(im, "いしいしし", font, 16)

    im.show()

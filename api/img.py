from PIL import Image, ImageDraw, ImageFont
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

def crop_center_image(crop_w, crop_h):
    """画像を中心で切り抜き"""
    im = Image.open("assets/img/gi/0.png")
    im_w, im_h = im.size
    # 画像の中心で切り抜き
    im_crop = im.crop((
        (im_w - crop_w) // 2,
        (im_h - crop_h) // 2 - 200,
        (im_w + crop_w) // 2,
        (im_h + crop_h) // 2 - 200
    ))
    return im_crop

def mask_img():
    im1 = Image.open("assets/img/gi/rs_0.png")
    im2 = Image.open("assets/img/gradient.png")
    mask = Image.new('L', im1.size, 0)
    im = Image.composite(im1, im2, mask)
    im.show()

if __name__ == "__main__":
    im = crop_center_image(2100, 756)

    # NOTE: 500x180のサイズにしたのはGithub上でちょうどいいサイズだったため
    im.resize((500, 180)).save("assets/img/gi/rs_0.png")

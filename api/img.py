from PIL import Image, ImageDraw, ImageFont
import base64
from io import BytesIO

# def create_image(text: str):
#     img = Image.new("RGB", (800, 600), (255, 255, 255))
#     draw = ImageDraw.Draw(img)
#     font = ImageFont.truetype("assets/fonts/gi.ttf", 36)
#     draw.text((10, 10), text=text, font=font, fill=(0, 0, 0))

#     buffered = BytesIO()
#     img.save(buffered, format="JPEG")
#     b64_img = base64.b64encode(buffered.getvalue()).decode('utf-8')
#     return b64_img

def text_image(path, text):
    im = Image.open(path)

    draw = ImageDraw.Draw(im)
    font = ImageFont.truetype("api/assets/fonts/gi.ttf", 36)
    draw.text((10, 10), text=text, font=font, fill=(0, 0, 0))

    buffered = BytesIO()
    im.save(buffered, format="PNG")
    buffered.seek(0)
    return buffered
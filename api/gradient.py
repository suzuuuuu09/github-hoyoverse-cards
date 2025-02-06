from PIL import Image, ImageDraw

# 画像サイズの定義
width, height = 500, 180

# グレースケール(L)モードで新しい画像を作成
image = Image.new('L', (width, height), color=255)

# 描画オブジェクトを作成
draw = ImageDraw.Draw(image)

# グラデーションを描画
for y in range(height):
    # 上半分: 黒から白へのグラデーション
    if y < height / 3:
        intensity = int(255 * (y / (height / 3)))
        color = intensity
    # 中央: 白
    elif y < 2 * height / 3:
        color = 255
    # 下半分: 白から黒へのグラデーション
    else:
        intensity = int(255 * ((y - 2 * height / 3) / (height / 3)))
        color = 255 - intensity
    
    # 水平線を描画
    draw.line([(0, y), (width, y)], fill=color)

# 画像を保存
image.save('gradient_image.png')
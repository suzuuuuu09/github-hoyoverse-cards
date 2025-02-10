from PIL import Image
import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from api import img

def convert_and_rename_images(folder_path: str = "assets/img/gi"):
    """
    指定フォルダ内の画像を500x180にリサイズし、PNGに変換して連番でリネーム
    
    Args:
        folder_path (str): 画像が格納されているフォルダのパス
    """
    try:
        # フォルダ内のファイル一覧を取得
        files = os.listdir(folder_path)
        # 画像ファイルのみをフィルタリング
        image_files = [f for f in files if f.lower().endswith(('.png', '.jpg', '.jpeg', '.webp'))]
        
        print(f"Found {len(image_files)} image files")
        
        # 連番で保存
        for i, filename in enumerate(image_files, 1):
            try:
                # 画像を開く
                image_path = os.path.join(folder_path, filename)
                with Image.open(image_path) as original_img:
                    # スマートクロップを適用
                    processed_img = img.smart_crop_image(original_img, 500, 180)
                    
                    # 新しいファイル名
                    new_filename = f"{i}.png"
                    new_path = os.path.join(folder_path, new_filename)
                    
                    # PNG形式で保存
                    processed_img.save(new_path, "PNG")
                    print(f"Processed and renamed: {filename} -> {new_filename}")
                    
                    # 元のファイルが新しいファイル名と異なる場合は削除
                    if filename != new_filename:
                        os.remove(image_path)
                        
            except Exception as e:
                print(f"Error processing {filename}: {e}")
                
        print("Processing completed successfully")
        
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    convert_and_rename_images()
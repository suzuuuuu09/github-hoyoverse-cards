from fastapi import FastAPI
from fastapi.responses import StreamingResponse
from img import create_image
import hoyo_api
import base64
from io import BytesIO

app = FastAPI()

@app.get("/api")
async def root(id: int = 1):
    return {"id": f"{id}"}

@app.get("/api/image")
# pillowで画像を作成しレスポンスさせる
async def image():
    user_info = await hoyo_api.fetch_user_data(819312869)
    if not user_info: return {"error": "Failed to fetch user data."}

    user_name = user_info["user_name"]
    level = user_info["adventure_rank"]
    signature = user_info["status_msg"]

    display_text = f"{user_name} Lv.{level} {signature}"
    b64_img = create_image(display_text)
    img_data = base64.b64decode(b64_img)
    img = BytesIO(img_data)

    return StreamingResponse(img, media_type="image/png")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, port=8000)
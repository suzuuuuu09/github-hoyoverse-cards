from fastapi import FastAPI
from fastapi.responses import StreamingResponse
from img import create_image
import base64
from io import BytesIO

app = FastAPI()

@app.get("/")
async def root(id: int = 1):
    return {"id": f"{id}"}

@app.get("/image")
async def image(text: str = "Hello, World!"):
    b64_img = create_image(text=text)
    img_data = base64.b64decode(b64_img)
    img = BytesIO(img_data)
    return StreamingResponse(img, media_type="image/png")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, port=8000)
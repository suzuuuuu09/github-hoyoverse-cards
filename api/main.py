from fastapi import FastAPI
from fastapi.responses import StreamingResponse
from api import img

app = FastAPI()

@app.get("/")
def index():
    return {"message": "Hello world!"}

@app.get("/image")
async def get_image(text: str="Hello world!"):
    im = img.text_image("api/assets/img/clip.png", text=text)

    return StreamingResponse(im, media_type="image/png")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, port=8000)
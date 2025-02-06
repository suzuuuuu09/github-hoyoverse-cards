from fastapi import FastAPI
from fastapi.responses import FileResponse


app = FastAPI()

@app.get("/")
def index():
    return {"message": "Hello world!"}

@app.get("/image")
async def get_image():
    return FileResponse("api/assets/img/clip.png", media_type="image/png")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, port=8000)
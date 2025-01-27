from fastapi import FastAPI

app = FastAPI()

@app.get("/api")
async def root(id: int = 1):
    return {"id": f"{id}"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, port=8000)
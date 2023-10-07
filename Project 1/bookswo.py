from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def firs_api():
    return {"message": "Hello Walt"}


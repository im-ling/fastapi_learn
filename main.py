from fastapi import FastAPI
import uvicorn
app = FastAPI()

# 路径参数无参数
# http://127.0.0.1:8000/user/me
@app.get("/user/me")
async def read_me():
    return {"me": '1'}

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=7766, workers=2)

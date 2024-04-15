from fastapi import FastAPI

app = FastAPI()

# 路径参数无参数
# http://127.0.0.1:8000/user/me
@app.get("/user/me")
async def read_me():
    return {"me": '1'}

# 路径参数指定类型
# http://127.0.0.1:8000/user/123456
# http://127.0.0.1:8000/user/qqq
@app.get("/user/{user_id}")
async def read_item(user_id: int):
    return {"user_id": user_id}

# @app.get("/user/{user_id}")
# async def read_item(user_id: str):
#     return {"user_id": user_id}


# 路径参数 enum 类型
from enum import Enum
class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"

# 路径参数指定类型
# http://127.0.0.1:8000/user_model/lenet
# http://127.0.0.1:8000/user_model/errorModel_name
@app.get("/user_model/{model_name}")
async def read_item(model_name: ModelName):
    return {"model": model_name}
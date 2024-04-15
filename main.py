from pydantic import BaseModel
from fastapi import FastAPI

app = FastAPI()

# 默认参数
@app.get("/items/")
async def read_item(skip: int = 0, limit: int = 10):
    fake_items_db = [{"item_name": "Foo"},
                     {"item_name": "Bar"},
                     {"item_name": "Baz"}]
    return fake_items_db[skip: skip + limit]
# http://127.0.0.1:8000/items/?skip=0&limit=2
# http://127.0.0.1:8000/items/?skip=20&limit=2
# http://127.0.0.1:8000/items/?skip=20


# 可选参数 必选参数
@app.get("/items/{item_id}")
async def read_user_item(item_id: str, needy: str):
    item = {"item_id": item_id, "needy": needy}
    return item
# http://127.0.0.1:8000/items/foo-item
# http://127.0.0.1:8000/items/foo-item?needy=bar


# 可选参数 q
@app.get("/items/{item_id}")
async def read_item(item_id: str, q: str | None = None, short: bool = False):
    item = {"item_id": item_id}
    if q:
        item.update({"q": q})
    if not short:
        item.update(
            {"description": "This is an amazing item that has a long description"}
        )
    return item
# http://127.0.0.1:8000/items/foo
# http://127.0.0.1:8000/items/foo?q=abs


# 类型转换
@app.get("/items/{item_id}")
async def read_item(item_id: str, short: bool = False):
    item = {"item_id": item_id}
    if not short:
        item.update(
            {"description": "This is an amazing item that has a long description"}
        )
    return item
# http://127.0.0.1:8000/items/foo?short=1 类型转换，1转为True
# http://127.0.0.1:8000/items/foo?short=True
# http://127.0.0.1:8000/items/foo?short=true
# http://127.0.0.1:8000/items/foo?short=TrUe
# http://127.0.0.1:8000/items/foo?short=on
# http://127.0.0.1:8000/items/foo?short=yes


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None
# 模型参数
@app.post("/items_model/")
async def create_item(item: Item):
    return item
# http://127.0.0.1:8000/items_model/?{name=abc,description=123,price=123}
# 需要通过body传参

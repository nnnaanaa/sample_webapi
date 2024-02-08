# http://ipaddress:port/users/100/items/100?q=100&short=True
# reference https://fastapi.tiangolo.com/ja/tutorial/query-params/

from typing import Union
from fastapi import FastAPI
app = FastAPI()

print("ui beam")

@app.get("/hello")
async def hello():
    return {"message": "hello world!"}

@app.get("/users/{user_id}/items/{item_id}")
async def read_user_item(
    user_id: int, item_id: str, q: Union[str, None] = None, short: bool = False
):
    item = {"item_id": item_id, "owner_id": user_id}
    if q:
        item.update({"q": q})
    if not short:
        item.update(
            {"description": "This is an amazing item that has a long description"}
        )
    return item

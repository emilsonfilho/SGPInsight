from fastapi import FastAPI
from typing import Union
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    nome: str
    value: float
    is_off: Union[bool, None] = None

itens_db = {}

@app.get("/itens")
async def get_items():
    return itens_db

@app.get("/itens/{item_id}")
async def get_item(item_id: int):
    if item_id in itens_db:
        return itens_db[item_id]
    else:
        return {
            "error": "Item not found"
        }

@app.put("/itens/{item_id}")
async def update_item(item_id: int, item: Item):
    itens_db[item_id] = item
    return {
        "msg": "Item atualizado ou criado com sucesso"
    }
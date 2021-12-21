from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder

from app.api_models import Item
from app.rpc_client import RpcClient

app = FastAPI()


@app.get('/')
def home():
    return 'Api is running'


@app.post("/items/")
def read_item(item: Item):
    sending_rpc = RpcClient()
    json_item = jsonable_encoder(item)
    response = sending_rpc.call(json_item)
    return response

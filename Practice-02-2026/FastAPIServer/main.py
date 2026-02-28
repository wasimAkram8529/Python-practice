from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

@app.get("/")
async def homePathHandler():
  return {
    "message": "Welcome to home page"
  }

@app.get("/ping")
async def pong():
  return {"message": "pong"}

@app.get("/users/{user_id}")
async def getUserDetail(user_id: int):
  print(user_id);
  return {"User ID": user_id, "name": "Alpha"}

@app.get("/products/{product_id}")
async def productHandler(product_id: int, price: int, limit: int):
  print(product_id)
  print(price)
  print(limit)
  return {"message": "Product details"}
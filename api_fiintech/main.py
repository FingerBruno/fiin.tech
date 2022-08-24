from fastapi import FastAPI
from symbolPrice import Price

app = FastAPI()


@app.get("/api/Price")
async def root(symbol:str):    
    return Price(symbol).getPrice()

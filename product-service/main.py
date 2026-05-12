from fastapi import FastAPI, HTTPException

app = FastAPI()

products = {
    "1": {"name": "Laptop", "price": 1000.0},
    "2": {"name": "Mouse", "price": 50.0}
}

@app.get("/products/{product_id}")
async def get_product(product_id: str):
    product = products.get(product_id)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product
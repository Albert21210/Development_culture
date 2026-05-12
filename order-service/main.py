import os
import httpx
from fastapi import FastAPI, HTTPException

app = FastAPI()

# Получаем URL из переменных окружения
PRODUCT_SERVICE_URL = os.getenv("PRODUCT_SERVICE_URL", "http://127.0.0.1:8000")
DISCOUNT_SERVICE_URL = os.getenv("DISCOUNT_SERVICE_URL", "http://127.0.0.1:8001")

@app.post("/orders/")
async def create_order(product_id: str, quantity: int, promo_code: str = None):
    async with httpx.AsyncClient() as client:
        # 1. Получаем товар
        prod_resp = await client.get(f"{PRODUCT_SERVICE_URL}/products/{product_id}")
        if prod_resp.status_code != 200:
            raise HTTPException(status_code=404, detail="Product not found")
        product = prod_resp.json()
        
        # 2. Получаем скидку
        price = product["price"]
        disc_resp = await client.post(f"{DISCOUNT_SERVICE_URL}/discounts/calculate", 
                                      json={"product_id": product_id, "quantity": quantity, "price": price, "promo_code": promo_code})
        discount_data = disc_resp.json()
        
        # 3. Расчет
        discount_percent = discount_data["discount_percent"]
        total_before = price * quantity
        discount_amount = total_before * (discount_percent / 100)
        total_after = total_before - discount_amount
        
        return {
            "product_id": product_id,
            "quantity": quantity,
            "price_per_unit": price,
            "total_before_discount": total_before,
            "discount_percent": discount_percent,
            "discount_amount": discount_amount,
            "final_total": total_after,
            "discount_reason": discount_data["reason"]
        }
import requests
import numpy as np
from fastapi import FastAPI

app = FastAPI()

def get_data_summary():
    """Пример функции, использующей внешние зависимости."""
    data = np.array([10, 20, 30, 40, 50])
    return {
        "mean": np.mean(data),
        "status": "active"
    }

@app.get("/")
def read_root():
    return get_data_summary()
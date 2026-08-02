from fastapi import FastAPI
import random

app = FastAPI()

@app.post("/tools/search_hotels")
async def search_hotels(data: dict):
    city = data.get("city")

    hotels = []

    for i in range(5):
        hotels.append({
            "name": f"{city} Hotel {i}",
            "price": random.randint(1000, 5000),
            "rating": round(random.uniform(3.5, 4.8), 1)
        })

    return hotels
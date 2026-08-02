from fastapi import FastAPI
import random

app = FastAPI()

@app.post("/tools/search_flights")
async def search_flights(data: dict):
    source = data.get("source")
    destination = data.get("destination")

    flights = []

    for i in range(5):
        flights.append({
            "airline": f"Airline-{i}",
            "price": random.randint(3000, 19000),
            "currency": random.choice(["INR", "USD"]),
            "duration": random.randint(1, 5)
        })

    return flights
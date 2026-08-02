from fastapi import FastAPI

app = FastAPI()

@app.post("/tools/search_places")
async def search_places(data: dict):
    city = data.get("city", "Unknown")

    # basic dataset (upgrade later)
    return [
        {"name": f"{city} Central Landmark", "rating": 4.7, "type": "landmark"},
        {"name": f"{city} Cultural Museum", "rating": 4.6, "type": "culture"},
        {"name": f"{city} Scenic Area", "rating": 4.8, "type": "nature"}
    ]
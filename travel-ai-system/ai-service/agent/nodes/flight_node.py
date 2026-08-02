print("flight_node loaded successfully")

from agent.tools.flight_tools import get_flights
from agent.tools.currency_tools import convert_currency

async def flight_node(state: dict):
    if "flights" not in state.get("intent", []):
        return state

    source = state["input"].get("source", "Delhi")
    destination = state["input"].get("destination", "Goa")

    flights = await get_flights(source, destination)

    normalized = []

    for f in flights:
        price = f.get("price", 0)
        currency = f.get("currency", "INR")

        if currency != "INR":
            res = await convert_currency(price, currency, "INR")
            price = res["converted_amount"]

        normalized.append({
            **f,
            "price": price,
            "currency": "INR"
        })

    # ✅ filter unrealistic prices
    filtered = [f for f in normalized if f["price"] < 50000]

    # ✅ rank by price + duration
    ranked = sorted(filtered, key=lambda x: (x["price"], x.get("duration", 0)))

    # ✅ take top 3
    best = ranked[:3]

    return {**state, "flights": best}
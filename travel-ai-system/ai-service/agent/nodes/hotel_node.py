print("hotel_node loaded successfully")  # debug

from agent.tools.hotel_tools import get_hotels

async def hotel_node(state: dict):
    if "hotels" not in state.get("intent", []):
        return state

    city = state["input"].get("destination", "Goa")

    hotels = await get_hotels(city)

    # ✅ filter good hotels
    filtered = [h for h in hotels if h["rating"] >= 4]

    # ✅ rank by price (cheap first) + better rating
    ranked = sorted(filtered, key=lambda x: (x["price"], -x["rating"]))

    # ✅ take top 3
    best = ranked[:3]

    return {**state, "hotels": best}
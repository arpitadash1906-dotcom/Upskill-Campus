print("places_node loaded successfully")  # debug

from agent.tools.places_tools import get_places

async def places_node(state: dict):
    if "places" not in state.get("intent", []):
        return state

    city = state["input"].get("destination", "Goa")

    places = await get_places(city)

    return {**state, "places": places}
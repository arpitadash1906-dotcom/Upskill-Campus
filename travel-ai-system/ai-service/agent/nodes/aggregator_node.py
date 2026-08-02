print("aggregator_node loaded successfully")  # debug

def aggregator_node(state: dict):
    return {
        "flights": state.get("flights"),
        "hotels": state.get("hotels"),
        "places": state.get("places"),
        "itinerary": state.get("itinerary")
    }
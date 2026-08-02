from agent.rag.retriever import retrieve_context

async def itinerary_node(state):
    if "places" not in state.get("intent", []):
        return state

    destination = state["input"].get("destination", "Unknown")
    places = state.get("places", [])

    if not places:
        return {**state, "itinerary": "No places found"}

    # 🔥 RAG context
    context = retrieve_context(destination)

    # 🔥 smarter grouping (basic logic)
    landmarks = [p for p in places if "landmark" in p.get("type", "").lower()]
    culture = [p for p in places if "culture" in p.get("type", "").lower()]
    nature = [p for p in places if "nature" in p.get("type", "").lower()]

    # fallback if categories missing
    day1 = landmarks[0]["name"] if landmarks else places[0]["name"]
    day2 = culture[0]["name"] if culture else (places[1]["name"] if len(places) > 1 else places[0]["name"])
    day3 = nature[0]["name"] if nature else (places[2]["name"] if len(places) > 2 else places[0]["name"])

    itinerary = f"""
3-Day Smart Travel Plan for {destination}:

Context:
{context}

Day 1 (Top Attractions):
- Visit {day1}

Day 2 (Culture & Exploration):
- Explore {day2}

Day 3 (Relax & Scenic):
- Relax at {day3}
"""
    print("ITINERARY NODE RUNNING")  # 👈 ADD
    return {**state, "itinerary": itinerary}
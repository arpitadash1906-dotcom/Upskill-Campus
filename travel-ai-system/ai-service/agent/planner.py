async def planner_node(state):
    query = state["input"]["query"].lower()

    intent = []

    if "flight" in query or "trip" in query:
        intent.append("flights")

    if "hotel" in query or "stay" in query or "trip" in query:
        intent.append("hotels")   # 👈 ADD THIS

    if "plan" in query or "trip" in query:
        intent.append("places")

    return {**state, "intent": intent}
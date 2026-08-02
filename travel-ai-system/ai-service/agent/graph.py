from langgraph.graph import StateGraph

from agent.planner import planner_node
from agent.nodes.flight_node import flight_node
from agent.nodes.hotel_node import hotel_node
from agent.nodes.places_node import places_node
from agent.nodes.itinerary_node import itinerary_node
from agent.nodes.aggregator_node import aggregator_node


def build_graph():
    graph = StateGraph(dict)

    # ✅ Register ALL nodes FIRST
    graph.add_node("planner", planner_node)
    graph.add_node("flights", flight_node)
    graph.add_node("hotels", hotel_node)
    graph.add_node("places", places_node)
    graph.add_node("itinerary", itinerary_node)
    graph.add_node("aggregator", aggregator_node)

    # ✅ Entry point
    graph.set_entry_point("planner")

    # ✅ STRICT SEQUENTIAL FLOW (NO PARALLEL)
    graph.add_edge("planner", "flights")
    graph.add_edge("flights", "hotels")
    graph.add_edge("hotels", "places")
    graph.add_edge("places", "itinerary")
    graph.add_edge("itinerary", "aggregator")

    return graph.compile()
from typing import TypedDict, List, Dict, Optional

class AgentState(TypedDict):
    input: dict
    intent: Optional[List[str]]
    flights: Optional[List[Dict]]
    hotels: Optional[List[Dict]]
    places: Optional[List[Dict]]
    result: Optional[dict]
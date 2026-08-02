from fastapi import FastAPI
from agent.graph import build_graph

app = FastAPI()
graph = build_graph()

@app.post("/plan")
async def plan(data: dict):
    try:
        result = await graph.ainvoke({"input": data})
        return result.get("result", result)
    except Exception as e:
        return {"error": str(e)}
from agent.rag.vectorstore import build_vectorstore

db = build_vectorstore()

def retrieve_context(query):
    docs = db.similarity_search(query, k=2)
    return "\n".join([d.page_content for d in docs])
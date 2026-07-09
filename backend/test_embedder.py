# from app.rag.embedder import embedder

# embedding = embedder.embed(
#     "FastAPI is a modern Python framework."
# )

# print(len(embedding))
# print(embedding[:10])

from app.rag.client import chroma_client

collection = chroma_client.get_collection(
    "startup"
)

print(collection.name)
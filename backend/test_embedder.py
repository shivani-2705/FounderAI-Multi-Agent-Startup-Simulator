# # from app.rag.embedder import embedder

# # embedding = embedder.embed(
# #     "FastAPI is a modern Python framework."
# # )

# # print(len(embedding))
# # print(embedding[:10])

# from app.rag.client import chroma_client

# collection = chroma_client.get_collection(
#     "startup"
# )

# print(collection.name)

# from app.rag.pdf_loader import pdf_loader

# text = pdf_loader.load(
#     "knowledge/startup/The Lean Startup - Erick Ries.pdf"
# )

# print(text[:1000])

from app.rag.chunker import chunker
from app.rag.pdf_loader import pdf_loader

text = pdf_loader.load(
    "knowledge/startup/The Lean Startup - Erick Ries.pdf"
)

chunks = chunker.split(text)

print(len(chunks))
print(chunks[0])
print(chunks[1])
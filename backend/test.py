#### Embedder

# from app.rag.embedder import embedder

# embedding = embedder.embed(
#     "FastAPI is a modern Python framework."
# )

# print(len(embedding))
# print(embedding[:10])




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

#####chunking 

# from app.rag.chunker import chunker
# from app.rag.pdf_loader import pdf_loader

# text = pdf_loader.load(
#     "knowledge/startup/The Lean Startup - Erick Ries.pdf"
# )

# chunks = chunker.split(text)

# print(len(chunks))
# print(chunks[0])
# print(chunks[1])

#######ingesting 


from app.rag.ingest import knowledge_ingestor

# knowledge_ingestor.ingest_folder(
#     folder="knowledge/startup",
#     collection_name="startup",
# )

knowledge_ingestor.ingest_folder(
    folder="knowledge/engineering",
    collection_name="engineering",
)

# knowledge_ingestor.ingest_folder(
#     folder="knowledge/product",
#     collection_name="product",
# )

# from app.rag.client import chroma_client

# collection = chroma_client.get_collection(
#     "startup"
# )

# print(collection.count())

# records = collection.peek(limit=2)

# print(records)

#from app.rag.retriever import retriever

# results = retriever.search(
#     collection_name="startup",
#     query="How should a startup validate an idea?",
# )


# print(results["documents"][0])

# from app.rag.retriever import retriever

# results = retriever.search(
#     collection_name="startup",
#     query="How should a startup validate an idea?",
#     top_k=5,
# )

# for i in range(len(results["documents"][0])):

#     print("=" * 80)

#     print(results["metadatas"][0][i])

#     print(results["distances"][0][i])

#     print(results["documents"][0][i][:500])


#context builder

# from app.rag.context_builder import context_builder

# context = context_builder.build(
#     collection_name="startup",
#     query="How should startups validate ideas?",
# )

# print(context)



# from app.rag.pdf_loader import pdf_loader

# text = pdf_loader.load("knowledge/engineering/SystemDesignInterview.pdf")

# print(len(text))
# print(text[:1000])
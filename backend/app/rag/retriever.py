from app.rag.client import chroma_client
from app.rag.embedder import embedder


class Retriever:

    def search(
        self,
        collection_name: str,
        query: str,
        top_k: int = 5,
    ):

        collection = chroma_client.get_collection(
            collection_name
        )

        query_embedding = embedder.embed(query)

        results = collection.query(
            query_embeddings=[query_embedding],
            n_results=top_k,
            include=[
                "documents",
                "metadatas",
                "distances",
            ],
        )

        return results


retriever = Retriever()
from app.rag.retriever import retriever


class ContextBuilder:

    def build(
        self,
        collection_name: str,
        query: str,
        top_k: int = 5,
    ) -> str:

        results = retriever.search(
            collection_name=collection_name,
            query=query,
            top_k=top_k,
        )

        contexts = []

        documents = results["documents"][0]
        metadatas = results["metadatas"][0]

        for doc, meta in zip(
            documents,
            metadatas,
        ):

            contexts.append(
                f"""
SOURCE:
{meta["source"]}

CONTENT:
{doc}
"""
            )

        return "\n\n".join(contexts)


context_builder = ContextBuilder()
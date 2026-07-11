import ollama


class Embedder:

    def __init__(
        self,
        model: str = "nomic-embed-text",
    ):
        self.model = model

    def embed(
        self,
        text: str,
    ) -> list[float]:

        response = ollama.embed(
            model=self.model,
            input=text,
        )

        return response["embeddings"][0]

    def embed_batch(
        self,
        texts: list[str],
    ) -> list[list[float]]:

        response = ollama.embed(
            model=self.model,
            input=texts,
        )

        return response["embeddings"]


embedder = Embedder()
import chromadb
from chromadb.config import Settings


class ChromaClient:

    def __init__(self):

        self.client = chromadb.PersistentClient(
            path="./chroma_db",
            settings=Settings(
                anonymized_telemetry=False
            ),
        )

    def get_collection(
        self,
        name: str,
    ):
        return self.client.get_or_create_collection(
            name=name
        )


chroma_client = ChromaClient()
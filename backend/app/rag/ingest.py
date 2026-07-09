from pathlib import Path
import uuid

from app.rag.client import chroma_client
from app.rag.chunker import chunker
from app.rag.pdf_loader import pdf_loader
from app.rag.embedder import embedder


class KnowledgeIngestor:

    def ingest_folder(
        self,
        folder: str,
        collection_name: str,
    ):

        collection = chroma_client.get_collection(
            collection_name
        )

        pdf_files = Path(folder).glob("*.pdf")

        for pdf in pdf_files:

            print(f"Ingesting {pdf.name}")

            text = pdf_loader.load(str(pdf))

            chunks = chunker.split(text)

            for index, chunk in enumerate(chunks):

                embedding = embedder.embed(chunk)

                collection.add(
                    ids=[str(uuid.uuid4())],
                    documents=[chunk],
                    embeddings=[embedding],
                    metadatas=[
                        {
                            "source": pdf.name,
                            "chunk": index,
                        }
                    ],
                )

        print("Done!")


knowledge_ingestor = KnowledgeIngestor()
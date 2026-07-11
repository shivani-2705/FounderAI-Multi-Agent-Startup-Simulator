from pathlib import Path
import uuid

from app.rag.client import chroma_client
from app.rag.chunker import chunker
from app.rag.embedder import embedder
from app.rag.pdf_loader import pdf_loader


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

            print("=" * 80)
            print(f"Ingesting {pdf.name}")

            try:

                text = pdf_loader.load(str(pdf))

                chunks = chunker.split(text)

                print(f"Total chunks: {len(chunks)}")

                

                BATCH_SIZE = 32

                for batch_start in range(0, len(chunks), BATCH_SIZE):

                    batch_chunks = chunks[
                        batch_start: batch_start + BATCH_SIZE
                    ]

                    embeddings = embedder.embed_batch(batch_chunks)

                    collection.add(
                        ids=[
                            str(uuid.uuid4())
                            for _ in batch_chunks
                        ],
                        documents=batch_chunks,
                        embeddings=embeddings,
                        metadatas=[
                            {
                                "source": pdf.name,
                                "chunk": batch_start + i,
                            }
                            for i in range(len(batch_chunks))
                        ],
                    )

                                   

            except Exception as e:

                print(
                    f"❌ Failed to ingest {pdf.name}"
                )

                print(e)

                continue

        print("=" * 80)
        print("Knowledge ingestion completed.")


knowledge_ingestor = KnowledgeIngestor()
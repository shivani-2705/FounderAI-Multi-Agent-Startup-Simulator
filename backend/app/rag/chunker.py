class Chunker:

    def __init__(
        self,
        chunk_size=800,
        overlap=150,
    ):
        self.chunk_size = chunk_size
        self.overlap = overlap

    def split(
        self,
        text: str,
    ):

        chunks = []

        start = 0

        while start < len(text):

            end = start + self.chunk_size

            chunks.append(
                text[start:end]
            )

            start += (
                self.chunk_size
                - self.overlap
            )

        return chunks


chunker = Chunker()
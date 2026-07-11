import re

from nltk.tokenize import sent_tokenize


class Chunker:

    def __init__(
        self,
        chunk_size: int = 800,
        overlap: int = 150,
        min_chunk_size: int = 200,
    ):
        self.chunk_size = chunk_size
        self.overlap = overlap
        self.min_chunk_size = min_chunk_size

    def clean_text(
        self,
        text: str,
    ) -> str:

        text = re.sub(r"\n{3,}", "\n\n", text)
        text = re.sub(r"[ \t]+", " ", text)

        return text.strip()

    def split(
        self,
        text: str,
    ):

        text = self.clean_text(text)

        paragraphs = text.split("\n\n")

        chunks = []

        current_chunk = ""

        for paragraph in paragraphs:

            paragraph = paragraph.strip()

            if not paragraph:
                continue

            if (
                len(current_chunk)
                + len(paragraph)
                < self.chunk_size
            ):

                if current_chunk:
                    current_chunk += "\n\n"

                current_chunk += paragraph

                continue

            if len(current_chunk) >= self.min_chunk_size:
                chunks.append(current_chunk)

            current_chunk = ""

            if len(paragraph) > self.chunk_size:

                sentences = sent_tokenize(paragraph)

                temp = ""

                for sentence in sentences:

                    if (
                        len(temp)
                        + len(sentence)
                        < self.chunk_size
                    ):

                        temp += " " + sentence

                    else:

                        if temp.strip():
                            chunks.append(temp.strip())

                        overlap = temp[-self.overlap :]

                        temp = overlap + " " + sentence

                if temp.strip():
                    chunks.append(temp.strip())

            else:

                current_chunk = paragraph

        if current_chunk.strip():
            chunks.append(current_chunk.strip())

        return chunks


chunker = Chunker()
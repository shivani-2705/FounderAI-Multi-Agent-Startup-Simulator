from pathlib import Path

from pypdf import PdfReader


class PDFLoader:

    def load(self, path: str) -> str:

        reader = PdfReader(path)

        text = ""

        for page in reader.pages:
            extracted = page.extract_text()

            if extracted:
                text += extracted + "\n"

        return text


pdf_loader = PDFLoader()
from app.knowledge.stores.base import BaseVectorStore


class ChromaVectorStore(BaseVectorStore):

    def add_documents(self, documents):
        raise NotImplementedError

    def search(self, query, top_k=5):
        raise NotImplementedError

    def delete_collection(self):
        raise NotImplementedError
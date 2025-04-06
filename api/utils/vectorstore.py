import uuid

from langchain.schema import Document
from langchain_chroma.vectorstores import Chroma
from langchain_huggingface import HuggingFaceEmbeddings

from api.constants import EMBEDDING_MODEL


class VectorStore:
    def __init__(self, file_path: str = './vectorstore') -> None:
        self.persist_dir = file_path

    def load_vector_store(self) -> Chroma:
        embeddings_model = HuggingFaceEmbeddings(model_name=EMBEDDING_MODEL)
        vectorstore = Chroma(
            persist_directory=self.persist_dir,
            embedding_function=embeddings_model
        )
        return vectorstore

    def create_vector_db(self, data: list[Document]) -> None:
        print('Creating vectorstore')
        embeddings_model = HuggingFaceEmbeddings(model_name=EMBEDDING_MODEL)
        Chroma.from_documents(
            documents=data,
            embedding=embeddings_model,
            ids=[str(uuid.uuid4()) for _ in data],
            persist_directory=self.persist_dir,
        )
        print('Vectorstore created')

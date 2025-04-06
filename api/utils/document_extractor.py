from langchain.schema import Document
from langchain.text_splitter import RecursiveCharacterTextSplitter


class DocumentExtractor:
    @staticmethod
    def load_and_split(file_path: str) -> list[Document]:
        print('Loading documents')
        with open(file_path, 'r') as file:
            paragraphs = file.read().split('\n\n')
        print('Documents loaded')
        print('Splitting documents')
        texts = [para for para in paragraphs if para.strip() != '']
        splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
        chunks = splitter.create_documents(texts)
        print('Documents loaded')
        return chunks

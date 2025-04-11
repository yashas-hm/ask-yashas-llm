from api.utils.document_extractor import DocumentExtractor
from api.utils.vectorstore import VectorStore

if __name__ == '__main__':
    chunks = DocumentExtractor.load_and_split('rag_data.txt')
    VectorStore().create_vector_db(chunks)

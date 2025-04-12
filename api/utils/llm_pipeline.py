import os

from langchain.chains import RetrievalQA
from langchain.prompts import PromptTemplate
from langchain_core.vectorstores.base import VectorStoreRetriever
from langchain_google_genai.llms import GoogleGenerativeAI

from api.constants import LLM_MODEL, AI_MSG_KEY, HUMAN_MSG_KEY, BOT, NAME
from api.utils.vectorstore import VectorStore


class LLMChain:
    retriever: VectorStoreRetriever

    def __init__(self, key: str) -> None:
        self.llm = GoogleGenerativeAI(model=LLM_MODEL, api_key=key)
        vector_store = VectorStore().load_vector_store()
        self.retriever = vector_store.as_retriever()

    @staticmethod
    def create_llm_pipeline() -> "LLMChain":
        api_token = os.environ.get("API_TOKEN")
        return LLMChain(key=api_token)

    def invoke_chain(self, query: str, history: list) -> str:
        llm_history = LLMChain.generate_history_context(history)
        qa_chain = RetrievalQA.from_chain_type(
            llm=self.llm,
            retriever=self.retriever,
            chain_type="stuff",
            chain_type_kwargs={"prompt": LLMChain.generate_prompt(llm_history)},
        )
        result = qa_chain.invoke({'query': query})
        return result['result']

    @staticmethod
    def generate_prompt(history: str) -> PromptTemplate:
        prompt_template = f"""
            Role: You are an AI assistant named {BOT}, for question-answering tasks about me ({NAME}).
            Use the following pieces of retrieved context to answer the question about me ({NAME}) or you ({BOT}).
            If you don't know the answer, just say that you can't assist with that.
            Keep the answer to the point follow the guidelines below.
            Guidelines:
            - If the query asks for a numerical value (e.g., amounts, percentages, dates), return only the relevant value.
            - For yes/no questions, answer with either 'Yes' or 'No' based on the context.
            - If no relevant information is available and the query is not a greeting or normal conversation, return 'I can't assist with that'.
            - Do not provide any additional commentary or filler text. Focus on precision and correctness from the context.
            - You can answer responses to greetings but nothing else that is not about me ({NAME}) or you
            Use the following pieces of retrieved context and relevant history if any to answer the question.
            
            Conversation History:
            {history}
            
            Context: 
            {{context}}
            
            Question: 
            {{question}}
        """
        return PromptTemplate(template=prompt_template, input_variables=['context', 'question'])

    @staticmethod
    def generate_history_context(history: list) -> list[str]:
        if len(history) == 0:
            return 'No History'
        chat_history = []
        for chat in history:
            if chat['role'].upper() == AI_MSG_KEY:
                chat_history.append(f'{BOT}: {chat["message"]}')
            elif chat['role'].upper() == HUMAN_MSG_KEY:
                chat_history.append(f'User: {chat["message"]}')
        return '\n'.join(chat_history)

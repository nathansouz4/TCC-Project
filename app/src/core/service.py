from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_community.vectorstores import Chroma
from langchain.retrievers.multi_vector import MultiVectorRetriever
from langchain.storage import InMemoryStore


from dotenv import load_dotenv
import os

load_dotenv('app/src/shared/.env')

GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')


gemini_embeddings = GoogleGenerativeAIEmbeddings(
    model="models/embedding-001", task_type="retrieval_document")

persist_directory = "./chroma_db/test_summaries"

# inicianlizing the vectorstore
vectorstore = Chroma(collection_name="summaries_nr10",
                     embedding_function=gemini_embeddings,
                     persist_directory=persist_directory)

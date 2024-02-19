import os
import sys
import constants
import openai
from langchain.chains import ConversationalRetrievalChain, RetrievalQA
from langchain.chat_models import ChatOpenAI
from langchain.document_loaders import DirectoryLoader, TextLoader
from langchain.embeddings import OpenAIEmbeddings
from langchain.indexes import VectorstoreIndexCreator
from langchain.indexes.vectorstore import VectorStoreIndexWrapper
from langchain.llms import OpenAI
from langchain.vectorstores import Chroma

os.environ['OPENAI_API_KEY'] = constants.APIKEY

query = sys.argv[1]
print(query)

loader = TextLoader('website_text.csv')
index = VectorstoreIndexCreator().from_loaders([loader])

print(index.query(query))


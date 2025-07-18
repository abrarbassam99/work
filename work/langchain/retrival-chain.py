from dotenv import load_dotenv
load_dotenv()

from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.documents import Document
from langchain.chains.combine_documents import create_stuff_documents_chain 
from langchain_community.document_loaders import WebBaseLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores.faiss import FAISS

def get_documents_from_web(url):
    loader=WebBaseLoader(url)
    docs= loader.load()
    splitter=RecursiveCharacterTextSplitter(
        chunck_size=200,
        chunk_overlap=20
    )
    splitDocs= splitter.split_documents(docs)
    print(len(splitDocs))
    return splitDocs

docs=get_documents_from_web("https://python.langchain.com/docs/introduction/")

docA=Document(
    page_content="Langchain Expression Language , LCEL "
)
model=ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0.4
)
prompt=ChatPromptTemplate.from_template("""
Answer the user question:
context:{context}
Question:{input}
""")
# chain = prompt | model

chain= create_stuff_documents_chain(
    llm=model,
    prompt=prompt
)
response=chain.invoke({
"input":"what is LCEL?",
"context":docs
})
print(response)
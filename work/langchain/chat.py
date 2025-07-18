from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate

from dotenv import load_dotenv
import os 
load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")
#Instaniate Model
llm= ChatOpenAI(
    api_key=api_key,
    model="gpt-4o-mini",
    temperature=0.7,
    max_tokens=1000,
    verbose=True,
)

#Prompet Template
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are an AI chef. Create a unique recipe based on the user's input."),
    ("human", "{input}")
])


#create LLm chain
chain= prompt | llm


response=chain.invoke({"input":"tometoes"})
print(response.content)
#for chunk in response:
#  print(chunk.content, end="",flush=True)


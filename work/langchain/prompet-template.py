from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
load_dotenv()
llm= ChatOpenAI(
    api_key=api_key,
    model="gpt-4o-mini",
    temperature=0.7,
    max_tokens=1000,
    verbose=True,
)
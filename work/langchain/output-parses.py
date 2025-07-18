from dotenv import load_dotenv
import os 
load_dotenv()
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser,CommaSeparatedListOutputParser
from pydantic import BaseModel, Field
import json

def call_string_output_parses():

    model=ChatOpenAI(model="gpt-4o-mini",temperature=0.7)
    prompt=ChatPromptTemplate.from_messages([
        ("system", "tell me a jock about the following subject"),
        ("human", "{input}")
    ]
)

    parser = StrOutputParser()
    chain= prompt | model | parser
    return chain.invoke({"input":"arabic"})

def call_list_output_parser():
    model=ChatOpenAI(model="gpt-4o-mini",temperature=0.7)
    prompt=ChatPromptTemplate.from_messages([
        ("system", "tell me a jock about the following subject"),
        ("human", "{input}")
    ]

    )
    parser= CommaSeparatedListOutputParser()
    chain =prompt | model | parser
    return chain.invoke(
        {
            "input":"happy"
        })

def call_json_output_parser():
    model = ChatOpenAI(model="gpt-4o-mini", temperature=0.7)

    class Person(BaseModel):
        name: str = Field(description="the name of the person")
        age: int = Field(description="the age of the person")

    parser = json(pydantic_object=Person)

    prompt = ChatPromptTemplate.from_messages([
        ("system", "Extract information from the following phrase.\nFormatting instructions: {format_instruction}"),
        ("human", "{phrase}")
    ])

    chain = prompt | model | parser

    return chain.invoke({
        "phrase": "Max is 30 years old",
        "format_instruction": parser.get_format_instructions()
    })
# print(call_json_output_parser())
print(call_list_output_parser().content)
print(type(call_string_output_parses()))
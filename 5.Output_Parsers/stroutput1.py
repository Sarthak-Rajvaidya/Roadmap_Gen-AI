from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

llm = ChatOpenAI(
    repo_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    task = "text-generation"
    
)

model = ChatOpenAI(llm =llm)

#1st prompt ->Detailed report

template1 = PromptTemplate(
    template='Write a detailed report on {topic}', 
    input_variables=['topic']
)


template2 = PromptTemplate(
    template='Write a 5 line summary on the folowing text ./n {text}',
    input_variables=['text']
)

parser = StrOutputParser()

chain = template1 | model | parser | template2 | model | parser

result = chain.invoke({'topic':'black hole'})

print(result)
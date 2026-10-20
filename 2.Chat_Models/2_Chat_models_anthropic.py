from langchain_anthropic import ChatAnthropic
from dotenv import load_dotenv

load_dotenv()

model = ChatAnthropic(model = 'claude-3.5-sonnet-20241022',temperature=0.7,max_tokens_to_sample=10)

result = model.invoke('What is the capital of india?')

print(result.content)
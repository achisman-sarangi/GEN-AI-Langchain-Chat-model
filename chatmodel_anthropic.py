from langchain_anthropic import ChatAnthropic
from dotenv import load_dotenv

load_dotenv()

model = ChatAnthropic(model="claude-3.5-sonnet-20241022", temperature=0.2, max_token = 10)

result = model.invoke("who is the president of the USA")

print(result.content)

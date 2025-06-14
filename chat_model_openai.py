from langchain_openai import  ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

chat_model = ChatOpenAI(model = "gpt-4",temperature = 1, max_tokens= 10)

response = chat_model.invoke("write a 5 line poem about football")
print(response.content)


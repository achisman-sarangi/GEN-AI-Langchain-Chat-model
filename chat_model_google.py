from langchain_google_genai import ChatGoogleGenerativeAI 
from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(model = "gemini-1.5-pro", temperature = 0.2)

result = model.invoke("who is the president of india")
print(result.content)
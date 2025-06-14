from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id = "starvector/starvector-1b-im2svg",
    task = "text-generation"
)

model = ChatHuggingFace(llm = llm)

result = model.invoke("who is the current president of india")

print(result.content)

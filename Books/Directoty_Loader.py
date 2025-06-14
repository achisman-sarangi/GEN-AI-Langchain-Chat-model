from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader

loader = DirectoryLoader(
    path = r"C:\Users\ACHISMAN\Desktop\Langchain models\2.Chat model\Books",
    glob = "*.pdf",
    loader_cls= PyPDFLoader
)

documents = loader.load()

print(len(documents))

print(documents[29].page_content)

print(documents[29].metadata)

print(documents)



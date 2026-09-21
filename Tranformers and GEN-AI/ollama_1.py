# Install the Ollama integration:
# !pip install -U langchain-ollama

# Import ollama
from langchain_ollama import OllamaLLM

# llm = OllamaLLM(model="llama3.2")
# llm = OllamaLLM(model="tinyllama")

response = llm.invoke("Explain RAG in simple terms")
print(response)





# Make sure TinyLlama is downloaded
# Open Command Prompt / Anaconda Prompt and run:
# ollama pull tinyllama

# Then you can test it:
# ollama run tinyllama



from langchain_ollama import OllamaLLM

llm = OllamaLLM(model="tinyllama")

response = llm.invoke("Explain what RAG is in simple terms")

print(response)



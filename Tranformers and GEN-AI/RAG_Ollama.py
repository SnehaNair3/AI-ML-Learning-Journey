

# ==========================================
# 1. Imports
# ==========================================

from langchain_ollama import OllamaLLM
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough


# ==========================================
# 2. Initialize TinyLlama
# ==========================================

llm = OllamaLLM(
    model="tinyllama"
)


# ==========================================
# 3. Test TinyLlama
# ==========================================

question = "When did India get Independence?"

response = llm.invoke(question)

print(response)


# ==========================================
# 4. Load PDF
# ==========================================

pdf_reader = PyPDFLoader("RAGPaper.pdf")

documents = pdf_reader.load()

print("Number of pages:", len(documents))


# ==========================================
# 5. Split PDF into chunks
# ==========================================

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=200
)

chunks = text_splitter.split_documents(documents)

print("Number of chunks:", len(chunks))


# ==========================================
# 6. Create embeddings
# ==========================================

embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)


# ==========================================
# 7. Create FAISS vector store
# ==========================================

db = FAISS.from_documents(
    documents=chunks,
    embedding=embeddings
)

print("FAISS vector store created.")


# ==========================================
# 8. Create retriever
# ==========================================

retriever = db.as_retriever(
    search_kwargs={"k": 3}
)


# ==========================================
# 9. Create RAG prompt
# ==========================================

prompt = ChatPromptTemplate.from_template("""
You are a helpful assistant.

Answer the question using ONLY the context provided below.

If the answer is not present in the context, say:
"I don't know based on the provided document."

Context:
{context}

Question:
{question}

Answer:
""")


# ==========================================
# 10. Format retrieved documents
# ==========================================

def format_docs(docs):
    return "\n\n".join(
        doc.page_content for doc in docs
    )


# ==========================================
# 11. Create RAG chain
# ==========================================

rag_chain = (
    {
        "context": retriever | format_docs,
        "question": RunnablePassthrough()
    }
    | prompt
    | llm
)


# ==========================================
# 12. Ask questions
# ==========================================

question = "What is a RAG-sequence model?"

answer = rag_chain.invoke(question)

print(answer)


# ==========================================
# 13. Another question
# ==========================================

question = "Who are the authors of this paper?"

answer = rag_chain.invoke(question)

print(answer)
import streamlit as st

# LangChain Imports
from langchain_community.document_loaders import SeleniumURLLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.vectorstores import InMemoryVectorStore
from langchain_ollama import OllamaEmbeddings
from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama.llms import OllamaLLM

# --- Configuration ---
st.set_page_config(page_title="AI Web Crawler", layout="centered")
st.title("🕷️ AI Web Crawler & Chat")

# --- Initialize Models ---
# We use @st.cache_resource so we don't reload the model object on every rerun
@st.cache_resource
def get_embeddings():
    return OllamaEmbeddings(model="llama3.2")

@st.cache_resource
def get_llm():
    return OllamaLLM(model="llama3.2")

embeddings = get_embeddings()
model = get_llm()

# --- Functions ---
def process_url(url):
    """Loads, splits, and indexes the URL."""
    status_text = st.empty()
    status_text.info(f"🕸️ Scraping {url}...")
    
    try:
        # 1. Load
        loader = SeleniumURLLoader(urls=[url])
        documents = loader.load()
        
        # 2. Split
        status_text.info("✂️ Splitting content...")
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=1000,
            chunk_overlap=200,
            add_start_index=True
        )
        chunked_documents = text_splitter.split_documents(documents)
        
        # 3. Index
        status_text.info("💾 Indexing to Vector Store...")
        vector_store = InMemoryVectorStore(embeddings)
        vector_store.add_documents(chunked_documents)
        
        status_text.success("✅ Ready to chat!")
        return vector_store
        
    except Exception as e:
        status_text.error(f"Error: {e}")
        return None

def answer_question(question, vector_store):
    """Retrieves context and generates an answer."""
    
    # Retrieve
    related_docs = vector_store.similarity_search(question)
    context = "\n\n".join([doc.page_content for doc in related_docs])
    
    # Generate
    template = """
    You are an assistant for question-answering tasks. Use the following pieces of retrieved context to answer the question. 
    If you don't know the answer, just say that you don't know. Use three sentences maximum and keep the answer concise.
    
    Question: {question} 
    Context: {context} 
    Answer:
    """
    prompt = ChatPromptTemplate.from_template(template)
    chain = prompt | model
    return chain.invoke({"question": question, "context": context})

# --- Session State Setup ---
if "vector_store" not in st.session_state:
    st.session_state.vector_store = None
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# --- UI Layout ---

url = st.text_input("Enter Website URL:", placeholder="https://example.com")

if st.button("Analyze Website"):
    if url:
        st.session_state.vector_store = process_url(url)
        st.session_state.chat_history = [] # Reset chat on new URL
    else:
        st.warning("Please enter a URL first.")

# --- Chat Interface ---

# Display chat history
for message in st.session_state.chat_history:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Handle new input
if question := st.chat_input("Ask a question about the website..."):
    
    # check if vector store exists
    if st.session_state.vector_store is None:
        st.error("Please analyze a website first!")
    else:
        # Display user message
        st.chat_message("user").write(question)
        st.session_state.chat_history.append({"role": "user", "content": question})
        
        # Generate and display assistant response
        with st.chat_message("assistant"):
            with st.spinner("Thinking..."):
                response = answer_question(question, st.session_state.vector_store)
                st.markdown(response)
        
        st.session_state.chat_history.append({"role": "assistant", "content": response})
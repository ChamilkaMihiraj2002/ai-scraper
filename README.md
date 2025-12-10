# 🕷️ AI Web Scraper

An intelligent web scraping and question-answering application that uses LangChain and Ollama to analyze websites and answer questions about their content.

## 📋 Description

This Streamlit-based application scrapes web content using Selenium, processes it into searchable chunks using LangChain, and leverages the Llama 3.2 model through Ollama to answer questions about the scraped content. The app creates a vector store from the website content, enabling semantic search and intelligent question answering.

## ✨ Features

- **Web Scraping**: Automatically scrapes content from any URL using Selenium
- **Intelligent Text Processing**: Splits content into optimized chunks for better retrieval
- **Vector Search**: Uses embeddings to find relevant content for your questions
- **AI-Powered Q&A**: Utilizes Llama 3.2 model for natural language understanding and response generation
- **Interactive Chat Interface**: User-friendly Streamlit interface with chat history
- **Context-Aware Responses**: Provides concise answers based on the scraped website content

## 🛠️ Technologies Used

- **Streamlit**: Web application framework
- **LangChain**: Framework for building LLM applications
- **Ollama**: Local LLM runtime (Llama 3.2)
- **Selenium**: Web scraping and automation
- **Vector Store**: In-memory storage for semantic search

## 📦 Installation

### Prerequisites

- Python 3.8 or higher
- [Ollama](https://ollama.ai/) installed on your system
- Llama 3.2 model pulled in Ollama

### Steps

1. Clone the repository:
```bash
git clone https://github.com/ChamilkaMihiraj2002/ai-scraper.git
cd ai-scraper
```

2. Install required dependencies:
```bash
pip install -r requirements.txt
```

3. Install and set up Ollama:
```bash
# Install Ollama from https://ollama.ai/
# Pull the Llama 3.2 model
ollama pull llama3.2
```

4. Install Chrome/Chromium browser (required for Selenium)

## 🚀 Usage

1. Start the Streamlit application:
```bash
streamlit run App/app.py
```

2. Open your browser and navigate to the provided local URL (typically `http://localhost:8501`)

3. Enter a website URL in the input field

4. Click "Analyze Website" to scrape and process the content

5. Once processing is complete, ask questions about the website in the chat interface

## 💡 Example Use Cases

- Quickly extract information from documentation pages
- Analyze blog posts or articles
- Get summaries of product pages
- Research competitor websites
- Extract key information from news articles

## 📁 Project Structure

```
ai-scraper/
├── App/
│   └── app.py          # Main Streamlit application
├── requirements.txt    # Python dependencies
├── LICENSE
└── README.md          # Project documentation
```

## 🔧 Configuration

The application uses the following default settings:

- **Chunk Size**: 1000 characters
- **Chunk Overlap**: 200 characters
- **LLM Model**: Llama 3.2 (via Ollama)
- **Embedding Model**: Llama 3.2 embeddings

You can modify these settings in `App/app.py` to suit your needs.

## ⚠️ Limitations

- Requires Ollama to be running locally
- Performance depends on your system's hardware (LLM inference can be slow on CPU)
- Some websites may block Selenium scraping
- JavaScript-heavy sites may require additional wait time for proper scraping

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📄 License

This project is licensed under the terms included in the LICENSE file.

## 👤 Author

ChamilkaMihiraj2002

## 🙏 Acknowledgments

- [LangChain](https://www.langchain.com/) for the powerful LLM framework
- [Ollama](https://ollama.ai/) for local LLM deployment
- [Streamlit](https://streamlit.io/) for the easy-to-use web framework
- Meta for the Llama models
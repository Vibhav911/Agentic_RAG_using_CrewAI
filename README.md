# 🤖 Agentic RAG using CrewAI

<div align="center">

![GitHub](https://img.shields.io/github/license/yourusername/agentic-rag-crewai)
![Python](https://img.shields.io/badge/python-v3.11+-blue.svg)
![CrewAI](https://img.shields.io/badge/CrewAI-Latest-green)

A powerful Retrieval-Augmented Generation (RAG) system built with CrewAI that intelligently searches through documents and falls back to web search when needed. Features local LLM support with deep-seek-r1 or llama 3.2!

</div>

## 🌟 Features

- 📚 Document-based search with RAG capabilities
- 🌐 Automatic fallback to web search
- 🤖 Local LLM support (deep-seek-r1 or llama 3.2)
- 🔄 Seamless integration with CrewAI
- 💨 Fast and efficient document processing
- 🎯 Precise answer synthesis

## 🔄 System Flow

Below is the detailed flow diagram of how the system processes queries and generates responses:

```mermaid
graph TD
    A[Start] --> B[Initialize Streamlit App]
    B --> C[Load LLM Model]
    C --> D[Initialize Session State]

    D --> E{PDF Uploaded?}
    E -->|Yes| F[Create DocumentSearchTool]
    E -->|No| G[Wait for PDF Upload]

    F --> H[Index PDF Document]
    H --> I[Create Crew]

    I --> J[Create Retriever Agent]
    I --> K[Create Response Synthesizer Agent]

    J --> L[Add Tools to Retriever Agent]
    L --> L1[PDF Search Tool]
    L --> L2[Web Search Tool]

    K --> M[Configure Response Agent]

    J & K --> N[Create Tasks]
    N --> N1[Retrieval Task]
    N --> N2[Response Task]

    N --> O[User Enters Query]

    O --> P[Process Query]
    P --> Q[Show User Message]
    Q --> R[Crew Kickoff]

    R --> S[Sequential Processing]
    S --> T1[Retriever Agent Searches]
    T1 --> T2[Response Agent Synthesizes]

    T2 --> U[Stream Response]
    U --> V[Update Chat History]

    V --> W[Wait for Next Query]
    W --> O
```

## 🛠️ System Architecture

The system consists of two main agents:

1. **Retriever Agent**:
   - Handles document searching
   - Manages web search fallback
   - Uses both PDF and web search tools

2. **Response Synthesizer Agent**:
   - Processes retrieved information
   - Generates coherent responses
   - Ensures context relevance

## 📚 Usage Examples

1. **Document Search**:
   - Upload your PDF document
   - Enter your query
   - Receive contextual answers from the document

2. **Web Search Fallback**:
   - System automatically detects when document search isn't sufficient
   - Seamlessly switches to web search
   - Combines information from multiple sources

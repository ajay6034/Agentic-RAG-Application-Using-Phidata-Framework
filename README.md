# Agentic RAG Project

## Description
- The Agentic RAG (Retrieval-Augmented Generation) project leverages the capabilities of Large Language Models (LLMs) and vector databases to answer queries based on the content extracted from a specific PDF document. This application uses a PDF URL to create a knowledge base, embedding the content into a vector database for efficient query answering and information retrieval.


- The main theme of the "Agentic RAG" project is to enhance information retrieval and response generation using Retrieval-Augmented Generation (RAG) techniques. This involves:

**Knowledge Extraction:** Automatically extracting and embedding text from PDF documents into a vector database.
**Vector Database Utilization:** Using a vector database to efficiently store and retrieve embedded text based on vector similarity.
**Query Answering with LLMs:** Leveraging Large Language Models (LLMs) to generate accurate responses based on the embedded knowledge from the PDF document.
- The project focuses on creating a robust system that can understand and respond to queries by integrating document-derived knowledge with the generative capabilities of LLMs, effectively blending document understanding with AI-driven interaction.

## Key Features
- **PDF Knowledge Extraction**: Automates the extraction and embedding of text from PDF documents.
- **Vector Database Integration**: Utilizes `LanceDb` for storing and searching embeddings.
- **LLM Interaction**: Employs Groq's LLM to generate responses based on the vector database's knowledge.

## Technologies Used
- Python 3.8+
- OpenAI API
- Groq API
- `LanceDb` for vector storage
- `dotenv` for environment management


# MediXtract - AI driven Retrieval-Augmented Generation Pipeline for Neurology-focused Literature Insight


A Retrieval-Augmented Generation (RAG)-based system for intelligently summarizing neurology research papers. This project combines vector similarity search with large language model (LLM)-powered summarization to help researchers and students navigate dense scientific literature with ease.

---

## Project Overview

This system enables users to ask natural language queries (like “What are the latest studies on Parkinson's biomarkers?”) and get academic-style, structured summaries extracted from real research papers. It is built using the RAG paradigm  combining neural semantic search with generative AI  and is optimized for domain-specific, scientific documents in neurology.
Unlike conventional keyword-based search engines, this assistant retrieves semantically relevant research chunks using vector embeddings and presents synthesized insights, not just raw links. It dramatically reduces information overload and saves time for domain-specific literature review.



---

## Technologies and frameworks used

- **Python** – Core scripting language for pipeline building
- **Retrieval-Augmented Generation (RAG)** – For contextualized, accurate response generation using real data.
- **FAISS** – Vector database for high speed vector similarity search over document embeddings.
- **SentenceTransformers (`all-MiniLM-L6-v2`)** – For generating dense semantic embeddings from chunked text.
- **PyMuPDF** – Extracts clean text from academic PDF papers.
- **Word-based Chunking Strategy** – Splits long papers into fixed-size 500-word segments to preserve context.
- **Backend** – Python flask 
- **Frontend** – HTML,CSS,Js
- **LLM**- Llama 3.8b

---

## System Overview

At its core, this project implements the **Retrieval-Augmented Generation (RAG)** architecture. RAG is a powerful technique that enhances the output of language models by grounding them in actual documents retrieved from a relevant knowledge base. Here's how the system operates:

1. **Document Ingestion**  
   Ingests a curated corpus of neurology research papers (`.txt` format) containing structured metadata (title, abstract, ID, body).

2. **Contextual Chunking**  
   Implements fixed-size, word-based segmentation (`500 words/chunk`) to preserve contextual integrity for downstream embedding.

3. **Semantic Embedding Generation**  
   Encodes each chunk into high-dimensional vectors using `all-MiniLM-L6-v2`  capturing semantic meaning beyond surface-level tokens.

4. **Vector Indexing via FAISS**  
   Indexes all embeddings using FAISS IndexFlatL2 for exact nearest-neighbor search based on L2 distance. Suitable for small to medium-scale datasets where brute-force search is still performant.

5. **Query Encoding & Retrieval**  
   Converts user queries into dense vector form and performs similarity search against the FAISS index to fetch top-`k` semantically aligned chunks.

6. **Retrieval-Augmented Generation (RAG)**  
   Supplies the retrieved chunks as input context to a large language model (e.g., GPT) to synthesize accurate, structured academic summaries.

7. **Answer Rendering**  
   Displays the generated response through a web-based UI with formal summaries, including paper titles, abstracts, and reference links.


This architecture brings together best practices in vector search, NLP, and LLM-based reasoning to create a powerful domain-specific retrieval tool.

**Sequence Diagram**

<img width="1920" height="1080" alt="Sequence_Diagram" src="https://github.com/user-attachments/assets/3507819c-1420-4c4c-a052-b90edc171ba8" />

---




## Features

-  **Semantic Search over Papers** – Retrieves the most relevant passages using vector similarity
-  **LLM-powered Summarization** – Produces academic-style summaries with structured sections
-  **Domain-optimized (Neurology)** – Tailored for summarizing biomedical and clinical papers
-  **High-speed FAISS Indexing** – Handles large-scale retrieval tasks with low latency
-  **Easily Scalable** – Add more papers or switch domains with minimal effort

##  Real-World Applications

This system is ideal for:

- **Clinical Research Assistance** – Quickly surfaces key findings across neurology research to inform practice.
- **Academic Study** – Helps students and educators access simplified summaries of complex papers.
- **Evidence-Based Medicine** – Supports fast, evidence-backed decision-making in clinical contexts.
- **Literature Review Acceleration** – Automates summarization for efficient survey of large paper sets.
- **AI-Powered Knowledge Extraction** – Enables large-scale semantic indexing and querying of scholarly documents.



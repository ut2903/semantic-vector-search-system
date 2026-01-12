
# Semantic Vector Search System

This repository presents a generalized, production-inspired implementation of a **semantic vector search system** built using dense text embeddings and FAISS-based similarity search.

The system is designed to retrieve relevant entities (such as products, content items, or catalog entries) based on semantic similarity rather than exact keyword matching. All proprietary identifiers, dataset names, and internal paths have been removed or abstracted.

---

## Overview

Traditional keyword search often fails when user queries and stored text differ lexically but share the same intent. This system addresses that limitation by:

- Encoding text into dense vector embeddings
- Indexing embeddings using FAISS for fast similarity search
- Retrieving the most relevant entities based on vector similarity
- Exposing the search functionality via a lightweight Flask API

The implementation reflects patterns commonly used in real-world production systems handling catalog-scale semantic retrieval.

---

## System Architecture

High-level flow:

```

User Query
↓
Text Preprocessing
↓
Embedding Generation (SentenceTransformer)
↓
FAISS Vector Search
↓
Metadata Lookup
↓
Ranked JSON Response

```

---

## Core Components

### 1. Text Preprocessing
Basic normalization is applied to input text to ensure consistency before embedding generation.

### 2. Embedding Model
The system uses a **SentenceTransformer** model (e.g., BGE-based encoders) to convert text into normalized dense vectors suitable for cosine similarity search.

### 3. FAISS Index
Precomputed embeddings are indexed using FAISS for efficient nearest-neighbor search at query time.

The index is loaded at application startup to support low-latency retrieval.

### 4. Metadata Mapping
FAISS indices return vector positions, which are mapped back to entity identifiers and metadata stored in a tabular dataset.

### 5. API Layer
A Flask-based HTTP API exposes a `/search` endpoint for querying the system.

---

## Project Structure

```

semantic-vector-search-system/
│
├── app/
│   └── api.py              # Flask API entry point
│
├── core/
│   ├── preprocess.py       # Text preprocessing
│   ├── model.py            # Embedding model loader
│   └── search.py           # FAISS search and result assembly
│
├── config/
│   └── paths.py            # Configurable paths and runtime settings
│
├── data/
│   └── sample_catalog.csv  # Example schema (optional)
│
├── requirements.txt
└── README.md

```

---

## API Usage

### Endpoint
```

GET /search?query=<text>

```

### Example
```

GET /search?query=wireless headphones

````

### Sample Response
```json
[
  {
    "Entity_Id": 10234,
    "Name": "Noise Cancelling Headphones",
    "Category": "Audio",
    "Brand": "GenericBrand",
    "Similarity_Score": 0.92
  }
]
````

---

## Configuration

All paths and runtime parameters are configurable via environment variables:

* `EMBEDDING_MODEL_PATH`
* `CATALOG_CSV_PATH`
* `FAISS_INDEX_PATH`
* `API_HOST`
* `API_PORT`

This allows the system to be adapted easily across environments without code changes.

---

## Scope & Limitations

**Included:**

* Semantic retrieval
* Dense vector search
* API-based querying
* Config-driven deployment

**Not included:**

* Authentication / authorization
* UI layer
* Query reranking
* Text generation (RAG)
* Hybrid keyword + vector search

These are intentional exclusions to keep the system focused and extensible.

---

## Intended Use

This repository is intended to demonstrate:

* Practical application of vector databases
* End-to-end semantic search pipelines
* Production-style API design
* Real-world engineering tradeoffs

It is not a toy example or tutorial, but a generalized system inspired by real deployment scenarios.

---

## License

MIT License

```


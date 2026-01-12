# config/paths.py

import os

# ===== MODEL CONFIG =====
EMBEDDING_MODEL_PATH = os.getenv(
    "EMBEDDING_MODEL_PATH",
    "/models/bge-base-en-v1.5"
)

# ===== DATA CONFIG =====
CATALOG_CSV_PATH = os.getenv(
    "CATALOG_CSV_PATH",
    "/data/catalog.csv"
)

FAISS_INDEX_PATH = os.getenv(
    "FAISS_INDEX_PATH",
    "/data/entity_index.faiss"
)

# ===== API CONFIG =====
API_HOST = os.getenv("API_HOST", "0.0.0.0")
API_PORT = int(os.getenv("API_PORT", 8200))

import numpy as np
import pandas as pd
import faiss

from core.preprocess import preprocess_text
from core.model import load_model
from config.paths import CATALOG_CSV_PATH, FAISS_INDEX_PATH

# Load model
model = load_model()

# Load DataFrame
data = pd.read_csv(CATALOG_CSV_PATH)

# Load FAISS index
faiss_index = faiss.read_index(FAISS_INDEX_PATH)

# Create mapping from index to entity ID
int_to_entity_id = {
    idx: eid for idx, eid in enumerate(data['entity_id'])
}

def get_query_embeddings(model, query):
    return model.encode(query, normalize_embeddings=True)

def search_faiss_index(query_vector, top_k=25):
    query_vector = np.array(query_vector).astype(np.float32)
    scores, indices = faiss_index.search(
        np.array([query_vector]), top_k
    )
    entity_ids = [int_to_entity_id[idx] for idx in indices[0]]
    return scores, entity_ids

def fetch_results(entity_ids, scores, data):
    results = []
    for entity_id, score in zip(entity_ids, scores[0]):
        row = data[data['entity_id'] == entity_id].iloc[0]
        results.append({
            "Entity_Id": entity_id,
            "Name": row['name'],
            "Category": row['category'],
            "Brand": row['brand'],
            "Similarity_Score": float(score)
        })
    return results

def entity_search(query):
    query = preprocess_text(query)
    query_vector = get_query_embeddings(model, query)
    scores, entity_ids = search_faiss_index(query_vector)
    return fetch_results(entity_ids, scores, data)

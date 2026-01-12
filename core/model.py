from sentence_transformers import SentenceTransformer
from config.paths import EMBEDDING_MODEL_PATH

def load_model():
    model = SentenceTransformer(EMBEDDING_MODEL_PATH).cuda()
    model.eval()
    return model

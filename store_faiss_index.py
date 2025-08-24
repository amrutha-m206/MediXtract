import json
import numpy as np
import faiss


with open("chunked_paper_embeddings.json", "r") as f:
    data = json.load(f)


embeddings = [item["embedding"] for item in data]
metadata = [item["metadata"] for item in data]


embedding_matrix = np.array(embeddings).astype("float32")


embedding_dim = embedding_matrix.shape[1]
index = faiss.IndexFlatL2(embedding_dim)

index.add(embedding_matrix)


faiss.write_index(index, "vector.index")


with open("metadata.json", "w") as f:
    json.dump(metadata, f)

print("✅ FAISS index and metadata saved.")



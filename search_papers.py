import faiss
import json
import numpy as np
from sentence_transformers import SentenceTransformer

# Load FAISS index
index = faiss.read_index("vector.index")

# Load metadata
with open("updated_metadata.json", "r") as f:
    metadata = json.load(f)

# Load the embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")


def search(query, k=5):
    # Convert query to embedding
    query_embedding = model.encode([query]).astype("float32")

    # Perform the search
    distances, indices = index.search(query_embedding, k)

    # Collect top-k results with metadata and avoid duplicates
    results = []
    seen_paper_ids = set()  # To track paper IDs and avoid duplicates

    for idx in indices[0]:
        paper_metadata = metadata[idx]
        paper_id = paper_metadata.get("paper_id")

        # Skip results that have already been added (based on paper_id)
        if paper_id not in seen_paper_ids:
            seen_paper_ids.add(paper_id)
            results.append(paper_metadata)  # fetch corresponding chunk metadata

    return results


# Example usage
if __name__ == "__main__":
    query = input("🔎 Enter your query: ")
    results = search(query, k=11)

    for i, item in enumerate(results, 1):
        print(f"\n📄 Result #{i}")
        print(f"Paper ID    : {item.get('paper_id')}")
        print(f"Title       : {item.get('title')}")
        print(f"PDF URL     : {item.get('pdf_link')}")

        # Check if 'text_chunk' exists
        text_chunk = item.get("text_chunk")
        if text_chunk:
            print(f"Text Snippet:\n{text_chunk[:300]}...")  # Show part of the text
        else:
            print("Text Snippet: Not available.")

import os
import json
from sentence_transformers import SentenceTransformer
import textwrap


model = SentenceTransformer("all-MiniLM-L6-v2")


input_folder = "extracted_papers"
output_json = "updated_metadata.json"
chunk_size = 500 


def chunk_text(text, chunk_size):
    words = text.split()
    return [
        " ".join(words[i : i + chunk_size]) for i in range(0, len(words), chunk_size)
    ]


# Final data list
data_to_store = []

for filename in os.listdir(input_folder):
    if filename.endswith(".txt"):
        filepath = os.path.join(input_folder, filename)

        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()

        try:
            paper_id = content.split("Paper ID: ")[1].split("\n")[0].strip()
            title = content.split("Title: ")[1].split("\n")[0].strip()
            abstract = content.split("Abstract: ")[1].split("\n\n")[0].strip()
            full_text = (
                content.split("Extracted Content:\n")[1]
                .split("\n\nPDF Link:")[0]
                .strip()
            )
            pdf_link = content.split("PDF Link: ")[1].strip()
        except Exception as e:
            print(f"⚠️ Error parsing {filename}: {e}")
            continue

        
        chunks = chunk_text(full_text, chunk_size)

        for i, chunk in enumerate(chunks):
            embedding = model.encode(chunk)

            data_to_store.append(
                {
                    "id": f"{paper_id}_chunk_{i+1}",
                    "embedding": embedding.tolist(),
                    "metadata": {
                        "paper_id": paper_id,
                        "chunk_index": i + 1,
                        "title": title,
                        "pdf_link": pdf_link,
                        "abstract": abstract,
                        "text_chunk": chunk,
                    },
                }
            )

        print(f"✅ Processed {filename} into {len(chunks)} chunks")

# Save all embeddings and metadata
with open(output_json, "w", encoding="utf-8") as f:
    json.dump(data_to_store, f, indent=2)

print(f"\n🎉 Done! Saved {len(data_to_store)} embedded chunks to {output_json}")

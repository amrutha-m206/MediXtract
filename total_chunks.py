import json

with open("chunked_paper_embeddings.json", "r") as f:
    data = json.load(f)

print(f" Total chunks loaded: {len(data)}")
# print(" First chunk example:")
# print(data[0])


with open("metadata.json", "r") as f:
    data = json.load(f)

print(f" Total chunks loaded: {len(data)}")

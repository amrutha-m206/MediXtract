from flask import Flask, render_template, request
from sentence_transformers import SentenceTransformer
import faiss
import json
import webbrowser
import threading
import requests
import os


index_path = os.path.join(os.path.dirname(__file__), "vector.index")
index = faiss.read_index(index_path)


GROQ_API_KEY = ""
GROQ_API_URL = "https://api.groq.com/openai/v1/chat/completions"
LLAMA_MODEL = "llama3-8b-8192"


with open("updated_metadata.json", "r") as f:
    metadata = json.load(f)

model = SentenceTransformer("all-MiniLM-L6-v2")

app = Flask(__name__, template_folder="../frontend")


def perform_search(query, k=5):
  
    query_embedding = model.encode([query]).astype("float32")
    distances, indices = index.search(query_embedding, k)

    results = []
    seen_paper_ids = set()

    for idx in indices[0]:
        paper_metadata = metadata[idx]
        paper_id = paper_metadata.get("paper_id")

        if paper_id not in seen_paper_ids:
            seen_paper_ids.add(paper_id)
            results.append(paper_metadata)

    return results


def summarize_with_llama(text):
   
    if not text.strip():
        return ""

    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json",
    }

    system_prompt = (
        "You are a helpful assistant that summarizes academic research papers. "
        "Please summarize the research paper into two clear and concise paragraphs. "
        "First is para 1 and second is para 2."
    )
    user_prompt = f"Please summarize the following research paper content:\n\n{text}"

    payload = {
        "model": LLAMA_MODEL,
        "messages": [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt},
        ],
        "temperature": 0.5,
        "max_tokens": 1024,
    }

    try:
      
        response = requests.post(GROQ_API_URL, headers=headers, json=payload)
        response.raise_for_status()

      
        summary = response.json()["choices"][0]["message"]["content"].strip()

       
        paragraphs = summary.split("\n")
        if len(paragraphs) < 2:
            return "\n".join(
                paragraphs[:2]
            ) 
        return summary

    except requests.exceptions.RequestException as e:
        print(f"Error making API request: {e}")
        return ""  # Return an empty string in case of error


@app.route("/")
def home():

    return render_template("index.html")


@app.route("/search", methods=["POST"])
def search_papers():
   
    try:
        query = request.form.get("query")
        results = perform_search(query, k=3)
        return render_template("results.html", results=results, query=query)
    except Exception as e:
        print(f"Error during search: {e}")
        return f"An error occurred during search: {str(e)}"


@app.route("/summarize", methods=["POST"])
def summarize_paper():
  
    try:
        paper_id = request.form.get("paper_id")

        # Find the paper from metadata
        paper = next((item for item in metadata if item["paper_id"] == paper_id), None)
        if not paper:
            return "Paper not found."

        full_text = paper.get("text_chunk", "")
        title = paper.get("title", "Untitled")

     
        max_chars = 6000
        if len(full_text) > max_chars:
            full_text = full_text[:max_chars]

        summary = summarize_with_llama(full_text)
        return render_template("summary.html", title=title, summary=summary)

    except Exception as e:
        print(f"Error during summarization: {e}")
        return f"An error occurred during summarization: {str(e)}"


def run_server():
   
    threading.Timer(1.5, lambda: webbrowser.open("http://127.0.0.1:8000")).start()
    app.run(host="127.0.0.1", port=8000, debug=True)


if __name__ == "__main__":
    run_server()

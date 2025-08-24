import requests
import fitz  # PyMuPDF for PDF text extraction
import os
import re

# Input and output file paths
input_file = "arxiv_brain_research1.txt"  # The file containing paper details
output_folder = "extracted_papers"
os.makedirs(output_folder, exist_ok=True)


# Function to download PDF
def download_pdf(pdf_url, paper_id):
    pdf_path = os.path.join(output_folder, f"{paper_id}.pdf")
    response = requests.get(pdf_url, stream=True)

    if response.status_code == 200:
        with open(pdf_path, "wb") as f:
            for chunk in response.iter_content(chunk_size=1024):
                f.write(chunk)
        return pdf_path
    else:
        print(f"❌ Failed to download: {pdf_url}")
        return None


# Function to extract text from a PDF
def extract_text_from_pdf(pdf_path):
    text = ""
    try:
        with fitz.open(pdf_path) as doc:
            for page in doc:
                text += page.get_text("text") + "\n"
    except Exception as e:
        print(f"⚠️ Error extracting text from {pdf_path}: {e}")
    return text.strip()


# Read the text file and process each paper
with open(input_file, "r", encoding="utf-8") as file:
    content = file.read()

# Extracting paper entries using regex
pattern = (
    r"Paper ID: (.+?)\nTitle: (.+?)\nAbstract: (.+?)\nLink: (.+?)\nPDF Link: (.+?)\n"
)
papers = re.findall(pattern, content, re.DOTALL)

for paper_id, title, abstract, link, pdf_link in papers:
    print(f"📄 Processing: {title}")

    # Download PDF
    pdf_path = download_pdf(pdf_link, paper_id)

    if pdf_path:
        # Extract text from PDF
        extracted_text = extract_text_from_pdf(pdf_path)

        # Save the extracted text to a new file
        text_output_path = os.path.join(output_folder, f"{paper_id}.txt")
        with open(text_output_path, "w", encoding="utf-8") as text_file:
            text_file.write(
                f"Paper ID: {paper_id}\nTitle: {title}\n\nAbstract: {abstract}\n\nExtracted Content:\n{extracted_text}\n\nPDF Link: {pdf_link}"
            )

        print(f"✅ Saved extracted content to {text_output_path}")

print("🎉 Processing complete!")

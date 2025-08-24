import feedparser
import requests
import re  # Import regex module

# Define related keywords for neurology and brain research
RELATED_KEYWORDS = [
    "neurology",
    "brain",
    "cognitive science",
    "neuroscience",
    "neurodegenerative diseases",
    "Alzheimer's",
    "Parkinson's",
    "mental disorders",
]


def fetch_arxiv_papers(queries, max_results_per_query=10):
    base_url = "http://export.arxiv.org/api/query"
    papers = set()  # Use a set to avoid duplicates

    for query in queries:
        params = {"search_query": f"all:{query}", "max_results": max_results_per_query}
        response = requests.get(base_url, params=params)

        if response.status_code != 200:
            print(f"Error fetching data for query: {query}")
            continue

        feed = feedparser.parse(response.text)

        for entry in feed.entries:
            title = entry.title
            abstract = entry.summary
            link = entry.link  # Example: https://arxiv.org/abs/2402.12345

            # Extract paper ID using regex
            match = re.search(r"arxiv\.org/abs/(\d+\.\d+)", link)
            paper_id = match.group(1) if match else "Unknown"

            pdf_link = f"https://arxiv.org/pdf/{paper_id}.pdf"  # Convert to PDF link

            paper_entry = f"Paper ID: {paper_id}\nTitle: {title}\nAbstract: {abstract}\nLink: {link}\nPDF Link: {pdf_link}\n"
            papers.add(paper_entry)  # Using set to remove duplicates

    # Save all results to a single file
    with open("arxiv_brain_research1.txt", "w", encoding="utf-8") as f:
        f.write("\n\n".join(papers))

    print("Saved all ArXiv results to arxiv_brain_research.txt")


# Fetch papers using multiple related terms
fetch_arxiv_papers(RELATED_KEYWORDS, max_results_per_query=3933)

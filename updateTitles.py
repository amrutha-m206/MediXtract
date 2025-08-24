import json


# Function to clean paper ID for matching
def clean_paper_id(paper_id):
    return paper_id.replace(".", "").replace("-", "")


# Load existing metadata
with open("metadata.json", "r") as f:
    metadata = json.load(f)

# Read the titles and paper IDs from arxiv_brainresrach1.txt
with open("arxiv_brain_research1.txt", "r") as f:
    lines = f.readlines()

# Initialize a list to store cleaned titles and their corresponding paper IDs
papers = {}
current_title = ""
current_paper_id = None

# Iterate through lines to construct titles, handling multi-line titles and paper IDs
for line in lines:
    line = line.strip()

    # Detect paper ID and title
    if line.startswith("Paper ID:"):  # Assuming Paper ID starts with 'Paper ID:'
        if current_paper_id and current_title:
            papers[clean_paper_id(current_paper_id)] = (
                current_title  # Save the current paper with its title
            )
        current_paper_id = line.replace("Paper ID:", "").strip()  # Get the paper ID
        current_title = ""  # Reset title for new paper
    elif line.startswith("Title:"):  # Start of title
        current_title = line.replace("Title:", "").strip()  # Clean and set title
    elif line.startswith("Abstract:"):  # Stop title when Abstract starts
        current_title = current_title.strip()  # Remove any extra spaces before stopping
        papers[clean_paper_id(current_paper_id)] = (
            current_title  # Save the title before abstract starts
        )
        current_title = (
            ""  # Reset title for the next paper after Abstract is encountered
        )
        continue
    elif current_title:  # If title exists, append to it
        current_title += " " + line.strip()

# Don't forget to add the last paper if Abstract was never encountered
if current_paper_id and current_title:
    papers[clean_paper_id(current_paper_id)] = current_title

# Update metadata with titles matched by paper ID
for item in metadata:
    paper_id = item.get("paper_id")  # Paper ID in metadata.json
    if paper_id:
        # Clean the paper ID in metadata to match the cleaned ID format
        cleaned_metadata_id = clean_paper_id(paper_id)

        # Check if cleaned paper ID exists in papers dictionary
        if cleaned_metadata_id in papers:
            item["title"] = papers[
                cleaned_metadata_id
            ]  # Update title for the matched paper

# Save the updated metadata to a new JSON file
with open("updated_metadata.json", "w") as f:
    json.dump(metadata, f, indent=4)

print("Titles updated successfully!")

import os


def count_txt_files(folder_path):
    count = 0
    for file_name in os.listdir(folder_path):
        if file_name.endswith(".txt"):
            count += 1
    return count


if __name__ == "__main__":
    folder = "extracted_papers"
    full_path = os.path.join(os.path.dirname(__file__), folder)

    total = count_txt_files(full_path)
    print(f"Total research papers: {total}")

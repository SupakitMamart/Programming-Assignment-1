import re
from collections import Counter
import os

# Define file paths
INPUT_FILE = "input/alice29.txt"  # Input file location
OUTPUT_DIR = "output"             # Output directory

# Ensure the output directory exists
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Define output file paths
CLEANED_FILE = os.path.join(OUTPUT_DIR, "cleaned.txt")
SENTENCES_FILE = os.path.join(OUTPUT_DIR, "sentences.txt")
WORDS_FILE = os.path.join(OUTPUT_DIR, "words.txt")
TOP10WORDS_FILE = os.path.join(OUTPUT_DIR, "top10words.txt")
TIME_COMPARES_FILE = os.path.join(OUTPUT_DIR, "time_compares.txt")

def preprocess_text():
    """
    Main function to preprocess and analyze text data.
    - Cleans the text.
    - Tokenizes into sentences and words.
    - Finds the most frequent words.
    - Outputs results to files.
    """
    # Load the input text
    with open(INPUT_FILE, "r") as file:
        text = file.read()

    # Step 1: Clean the text
    cleaned_text = re.sub(r"[^a-zA-Z\s]", "", text)  # Remove punctuation
    cleaned_text = cleaned_text.lower()  # Convert to lowercase

    # Save cleaned text
    with open(CLEANED_FILE, "w") as file:
        file.write(cleaned_text)

    # Step 2: Tokenize sentences and words
    sentences = re.split(r"[.!?]\s+", text)  # Simple sentence splitting
    words = cleaned_text.split()  # Split into words

    # Save tokenized sentences
    with open(SENTENCES_FILE, "w") as file:
        file.write("\n".join(sentences))

    # Save tokenized words
    with open(WORDS_FILE, "w") as file:
        file.write("\n".join(words))

    # Step 3: Frequency analysis
    word_counts = Counter(words)
    top_10_words = word_counts.most_common(10)

    # Save top 10 words
    with open(TOP10WORDS_FILE, "w") as file:
        for word, count in top_10_words:
            file.write(f"{word}: {count}\n")

    # Optional: Save performance comparison (skipped for simplicity)
    with open(TIME_COMPARES_FILE, "w") as file:
        file.write("Performance comparison not implemented in this version.\n")

    print("Text processing complete. Results saved in the 'output' directory.")

if __name__ == "__main__":
    preprocess_text()

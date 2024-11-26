import re
import time
from collections import Counter
import nltk
from nltk.tokenize import sent_tokenize, word_tokenize

# Ensure NLTK data is downloaded (only needs to be done once)
nltk.download('punkt')

# File paths
INPUT_FILE = "input/alice29.txt"
OUTPUT_FILE = "output/time_compares.txt"

# Load the input text
with open(INPUT_FILE, "r") as file:
    text = file.read()

# Measure performance of manual methods
start_manual = time.time()
cleaned_text = re.sub(r"[^a-zA-Z\s]", "", text).lower()
manual_sentences = re.split(r'[.!?]\s+', text)
manual_words = cleaned_text.split()
manual_word_counts = Counter(manual_words)
manual_top_10 = manual_word_counts.most_common(10)
end_manual = time.time()

# Measure performance of NLTK methods
start_nltk = time.time()
nltk_sentences = sent_tokenize(text)
nltk_words = word_tokenize(cleaned_text)
nltk_word_counts = Counter(nltk_words)
nltk_top_10 = nltk_word_counts.most_common(10)
end_nltk = time.time()

# Compare performance
comparison_results = [
    {"Method": "Manual Tokenization", "Execution Time (s)": end_manual - start_manual},
    {"Method": "NLTK Tokenization", "Execution Time (s)": end_nltk - start_nltk},
]

# Display results as a table
print(f"{'Method':<25}{'Execution Time (s)':<20}")
print("=" * 45)
for result in comparison_results:
    print(f"{result['Method']:<25}{result['Execution Time (s)']:<20.6f}")

# Save results to a file
with open(OUTPUT_FILE, "w") as file:
    file.write(f"{'Method':<25}{'Execution Time (s)':<20}\n")
    file.write("=" * 45 + "\n")
    for result in comparison_results:
        file.write(f"{result['Method']:<25}{result['Execution Time (s)']:<20.6f}\n")

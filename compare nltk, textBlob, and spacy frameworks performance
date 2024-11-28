import time
import re
from collections import Counter
import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from textblob import TextBlob
import spacy

# Ensure NLTK data is downloaded
nltk.download('punkt')

# Load SpaCy model
nlp = spacy.load("en_core_web_sm")

# File path
INPUT_FILE = "alice29.txt"
OUTPUT_FILE = "performance_comparison.txt"

# Load the text
with open(INPUT_FILE, "r") as file:
    text = file.read()

# Clean text (remove special characters, lowercase)
cleaned_text = re.sub(r"[^a-zA-Z\s]", "", text).lower()

# === Measure performance of NLTK ===
start_nltk = time.time()
nltk_sentences = sent_tokenize(text)
nltk_words = word_tokenize(cleaned_text)
nltk_word_counts = Counter(nltk_words)
nltk_top_10 = nltk_word_counts.most_common(10)
end_nltk = time.time()
nltk_time = end_nltk - start_nltk

# === Measure performance of TextBlob ===
start_textblob = time.time()
textblob = TextBlob(text)
textblob_sentences = textblob.sentences
textblob_words = textblob.words.lower()
textblob_word_counts = Counter(textblob_words)
textblob_top_10 = textblob_word_counts.most_common(10)
end_textblob = time.time()
textblob_time = end_textblob - start_textblob

# === Measure performance of SpaCy ===
start_spacy = time.time()
spacy_doc = nlp(text)
spacy_sentences = [sent.text for sent in spacy_doc.sents]
spacy_words = [token.text.lower() for token in spacy_doc if token.is_alpha]
spacy_word_counts = Counter(spacy_words)
spacy_top_10 = spacy_word_counts.most_common(10)
end_spacy = time.time()
spacy_time = end_spacy - start_spacy

# === Compare results ===
performance_results = [
    {"Framework": "NLTK", "Execution Time (s)": nltk_time},
    {"Framework": "TextBlob", "Execution Time (s)": textblob_time},
    {"Framework": "SpaCy", "Execution Time (s)": spacy_time},
]

# Print performance comparison table
print(f"{'Framework':<15}{'Execution Time (s)':<20}")
print("=" * 35)
for result in performance_results:
    print(f"{result['Framework']:<15}{result['Execution Time (s)']:<20.6f}")

# Save performance results to a file
with open(OUTPUT_FILE, "w") as file:
    file.write(f"{'Framework':<15}{'Execution Time (s)':<20}\n")
    file.write("=" * 35 + "\n")
    for result in performance_results:
        file.write(f"{result['Framework']:<15}{result['Execution Time (s)']:<20.6f}\n")

# Save top 10 words for each framework to file
with open("top10words.txt", "w") as file:
    file.write("Top 10 Words (NLTK):\n")
    for word, count in nltk_top_10:
        file.write(f"{word}: {count}\n")
    file.write("\nTop 10 Words (TextBlob):\n")
    for word, count in textblob_top_10:
        file.write(f"{word}: {count}\n")
    file.write("\nTop 10 Words (SpaCy):\n")
    for word, count in spacy_top_10:
        file.write(f"{word}: {count}\n")

# Text Preprocessing and Analysis Script

This script processes and analyzes a given text file. It performs the following tasks:
1. Cleans the text by removing punctuation and converting it to lowercase.
2. Tokenizes the text into sentences and words.
3. Identifies the top 10 most frequent words in the text.
4. Saves the cleaned text, tokenized data, and word frequency analysis to output files.

## Requirements
- Python 3.x
- No external libraries are required for this script.

## Directory Structure
```plaintext
your-repo/
├── input/
│   └── alice29.txt    # Input file (replace with your own)
├── output/            # Output directory (generated automatically)
│   ├── cleaned.txt
│   ├── sentences.txt
│   ├── words.txt
│   ├── top10words.txt
│   ├── time_compares.txt
├── preprocess_text.py # Python script
└── README.md          # This file

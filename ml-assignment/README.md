# Trigram Language Model

Trigram Language Model Assignment

This project implements a Trigram (N-Gram) Language Model in Python. It is designed to train on text corpora (like books from Project Gutenberg) and generate new, probabilistic text based on the learned patterns.

Project Structure

ml-assignment/

├── data/                    # Data storage 

├── src/ 

│   ├── generate.py          # Entry point script to run the model 

│   └── ngram_model.py       # The core TrigramModel class 

├── tests/ 

│   └── test_ngram.py        # Unit tests 

├── evaluation.md            # Design choices 

├── README.md                # This file 

└── requirements.txt         # Library required 

Setup Instructions

Prerequisites:
Create a Virtual Environment
Install Dependencies:
You need to download book and pytest for testing
pip install -r requirements.txt

How to Run the Model
Run the generate.py script

What happens:
It initializes the TrigramModel
It trains on the text
It prints generated text to the console

How to Run Tests
To run the tests, execute the following command from the ml-assignment directory:
cd ml-intern-assessment/ml-assignment
python3 -m pytest

Note: Using python -m pytest is important because it ensures Python can find the src module correctly without import errors

Design & Evaluation

For a detailed explanation of the design choices (why I used dictionaries, how I handled padding, etc), please refer to evaluation.md

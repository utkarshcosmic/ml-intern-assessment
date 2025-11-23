# Trigram Language Model

Trigram Model Evaluation & Design Choices

Overview: This document outlines the design decisions, trade-offs, and implementation details for the Trigram Language Model. The goal was to build a system that is not only mathematically correct but also readable, efficient, and easy to extend.

Key Design Choices

1. Data Structure: Nested Dictionaries vs. Sparse Matrices

For storing n-gram counts, I had to choose between a dense matrix (like a NumPy array) and a hash map (dictionary)
Decision: I used a nested dictionary structure: collections.defaultdict(Counter)
Reasoning: Language is sparse. Most word combinations (e.g., "banana republic spaceship") never occur. A matrix would be huge and mostly empty (zeros). A dictionary only stores observed pairs, making it memory-efficient.

2. Preprocessing Strategy

Raw text from books like Alice in Wonderland is messy. It contains formatting, distinct casing (Alice vs. alice), and punctuation.
Decision: I implemented a strict cleaning pipeline
Lowercasing: To ensure "The" and "the" are treated as the same context
Regex Cleaning: I used re.sub(r'[^\w\s]', '', text) to strip punctuation. This simplifies the vocabulary size significantly, which is crucial for a small model to generate coherent text.
Newline Removal: I replaced newlines with spaces to treat the entire book as a continuous stream of thought, rather than a list of disconnected lines

3. The "N-1" Padding Logic

A common pitfall in N-gram models is handling the start of sentences
Decision: For a Trigram model ($N=3$), I padded the input with two ($N-1$) <START> tokens
Reasoning: To predict the very first word of the text, the model needs a history of size 2. Without ['<START>', '<START>'], the model would be unable to generate the opening of a sentence. I also added a <STOP> token so the generation loop knows when to naturally end a sentence.

4. Probabilistic Generation (Weighted Sampling)

When generating text, there are two main strategies: "Greedy" (always pick the most likely word) and "Stochastic" (pick based on probability)
Decision: I used Stochastic sampling via random.choices(weights=counts)
Reasoning: Greedy search produces repetitive, boring loops. By using the counts as weights, the model mirrors the distribution of the original author. If "Alice" is followed by "said" 80% of the time and "thought" 20% of the time, my generator preserves this ratio. This makes the output feel more organic and less robotic.
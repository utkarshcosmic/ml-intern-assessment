import random
import re
from collections import defaultdict, Counter            

class TrigramModel:
    def __init__(self):
        # We store counts in a nested dictionary: 
        # model[(word1, word2)][word3] = count
        self.model = defaultdict(Counter)

    def fit(self, text):
        # Clean: Lowercase and remove punctuation (keep only words and spaces)
        text = text.lower()
        text = re.sub(r'[^\w\s]', '', text) 
        
        # Tokenize: Split into words
        words = text.split()

        #  Pad: Trigrams need 2 start tokens to predict the 1st real word
        tokens = ["<START>", "<START>"] + words + ["<STOP>"]

        # Count: Slide over the text and store counts
        for i in range(len(tokens) - 2):
            w1 = tokens[i]
            w2 = tokens[i+1]
            w3 = tokens[i+2]
            
            bigram = (w1, w2)
            self.model[bigram][w3] += 1

    def generate(self, max_length=50):

        # Start with the initial padding
        current_bigram = ("<START>", "<START>")
        result = []

        for _ in range(max_length):
            if current_bigram not in self.model:
                break # Stop if we hit a dead end

            # Get possible next words and their counts
            candidates = self.model[current_bigram]
            words = list(candidates.keys())
            counts = list(candidates.values())

            # Probabilistically pick the next word using counts as weights
            next_word = random.choices(words, weights=counts, k=1)[0]

            if next_word == "<STOP>":
                break # Stop if the model finishes the sentence

            result.append(next_word)
            
            # Update context: (w1, w2) -> (w2, new_word)
            current_bigram = (current_bigram[1], next_word)

        return " ".join(result)

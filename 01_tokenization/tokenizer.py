import re
class SimpleTokenizerV1:
    def __init__(self, vocab):
        # vocab is a dictionary like {"hello": 0, "world": 1}
        # str_to_int: word → number (directly from vocab)
        self.str_to_int = vocab
        # int_to_str: number → word (reverse of vocab)
        # we flip the key-value pairs using dictionary comprehension
        self.int_to_str = {i:s for s,i in vocab.items()}

    def encode(self, text):
        # Step 1: Split text into tokens (words + punctuation)
        preprocessed = re.split(r'([,.?_!"()\']|--|\s)', text)
        
        # Step 2: Remove empty strings and extra whitespace
        preprocessed = [
            item.strip() for item in preprocessed if item.strip()
        ]
        # Step 3: Convert each token to its number using str_to_int
        ids = [self.str_to_int[s] for s in preprocessed]
        return ids
    def decode(self, ids):
        # Step 1: Convert each number back to its token using int_to_str
        # Step 2: Join all tokens with a space
        text = " ".join([self.int_to_str[i] for i in ids])
        # Step 3: Fix spacing before punctuation
        # e.g. "Hello , world" → "Hello, world"
        text = re.sub(r'\s+([,.?!"()\'])', r'\1', text)
        return text
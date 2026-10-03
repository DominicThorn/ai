import nltk
nltk.download('punkt')
from nltk.tokenize import word_tokenize

text = "Artificial Intelligence is a powerful technology."
tokens = word_tokenize(text)

print("Original Text:")
print(text)
print("\nTokens:")
print(tokens)
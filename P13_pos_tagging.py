import nltk
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
from nltk.tokenize import word_tokenize

text = "The student is reading a book."
words = word_tokenize(text)
pos_tags = nltk.pos_tag(words)

print("Original Text:")
print(text)
print("\nParts of Speech:")
print(pos_tags)
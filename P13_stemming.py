import nltk
nltk.download('punkt')
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize

text = "The students are studying and playing games."
words = word_tokenize(text)

stemmer = PorterStemmer()
stemmed_words = [stemmer.stem(word) for word in words]

print("Original Text:")
print(text)
print("\nAfter Stemming:")
print(stemmed_words)
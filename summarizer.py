import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from nltk.probability import FreqDist

# Basic text summarization: extracts first N sentences
def summarize_text(text, num_sentences=3):
    sentences = sent_tokenize(text)
    return " ".join(sentences[:num_sentences])

# Extracts most frequent words excluding stopwords
def extract_keywords(text):
    stop_words = set(stopwords.words('english'))
    words = word_tokenize(text)
    filtered_words = [w.lower() for w in words if w.isalnum() and w.lower() not in stop_words]
    freq_dist = FreqDist(filtered_words)
    return [word for word, freq in freq_dist.most_common(5)]

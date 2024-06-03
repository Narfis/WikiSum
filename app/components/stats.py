from collections import Counter
import re
import string

class Statistics():
    def get_most_used_words(self, wiki_content, n=10):

        text = re.sub(r'<[^>]+>', '', wiki_content)
        text = text.translate(str.maketrans('', '', string.punctuation)).lower()
        words = text.split()

        counter = Counter(words)
        most_used_words = counter.most_common(10)
        return most_used_words
    
    def get_mean_word_length(self, wiki_content):
        text = re.sub(r'<[^>]+>', '', wiki_content)
        text = text.translate(str.maketrans('', '', string.punctuation)).lower()
        words = text.split()
        total_length = sum(len(word) for word in words)
        return total_length / len(words)

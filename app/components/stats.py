from collections import Counter
import re
import string

class Statistics():
    # It's statistics about a wikipedia page

    def get_most_used_words(self, wiki_content, n=10):
        # Returns the most used words in the wikipedia page

        text = re.sub(r'<[^>]+>', '', wiki_content)
        text = text.translate(str.maketrans('', '', string.punctuation)).lower()
        words = text.split()

        counter = Counter(words)
        most_used_words = counter.most_common(10)
        print(most_used_words)
        return most_used_words
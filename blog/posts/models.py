import re
from collections import Counter
from django.db import models

# Create your models here.

# Feel free to move this to a new file if you are carrying out the 'tags' calculation there
stopWords = [
    "#", "##", "a", "about", "above", "after", "again", "against", "all", "am",
    "an", "and", "any", "are", "aren't", "as", "at", "be", "because", "been",
    "before", "being", "below", "between", "both", "but", "by", "can't", "cannot",
    "could", "couldn't", "did", "didn't", "do", "does", "doesn't", "doing", "don't",
    "down", "during", "each", "few", "for", "from", "further", "had", "hadn't",
    "has", "hasn't", "have", "haven't", "having", "he", "he'd", "he'll", "he's",
    "her", "here", "here's", "hers", "herself", "him", "himself", "his", "how",
    "how's", "i", "i'd", "i'll", "i'm", "i've", "if", "in", "into", "is", "isn't",
    "it", "it's", "its", "itself", "let's", "me", "more", "most", "mustn't", "my",
    "myself", "no", "nor", "not", "of", "off", "on", "once", "only", "or", "other",
    "ought", "our", "ours", "ourselves", "out", "over", "own", "same", "shan't", "she",
    "she'd", "she'll", "she's", "should", "shouldn't", "so", "some", "such", "than", "that",
    "that's", "the", "their", "theirs", "them", "themselves", "then", "there", "there's",
    "these", "they", "they'd", "they'll", "they're", "they've", "this", "those", "through",
    "to", "too", "under", "until", "up", "very", "was", "wasn't", "we", "we'd", "we'll",
    "we're", "we've", "were", "weren't", "what", "what's", "when", "when's", "where",
    "where's", "which", "while", "who", "who's", "whom", "why", "why's", "with", "won't",
    "would", "wouldn't", "you", "you'd", "you'll", "you're", "you've", "your", "yours",
    "yourself", "yourselves"
]



# we assume that all posts are formatted in the same way ie:
"""
===
Title: some title
Author: some author
Slug: filename-minus-.md
===
markdown content....
"""
class Post(models.Model):
    content = models.TextField()
    slug = models.CharField(max_length=255)

    """ 
        no try catching here because of the assumption that all 
        posts are formatted in the same way as if it were a DB
        both of the title and only_content methods
        use an assumption about the number of lines for the title etc
    """

    def title(self):
        lines = self.content.split('\n')
        title = lines[1].replace('Title: ', '', 1)
        return title
  
    def only_content(self):
        notags = re.compile('<.*?>') 
        lines = self.content.split('\n')
        content = lines[5:]
        only_content = "\n".join(content)
        return re.sub(notags, '', only_content)

    def tags(self):
        all_words_lowercase = [w.lower() for w in re.sub(r"[^a-zA-Z ']", '', self.content).split()]
        stop_words_lowercase = [word.lower() for word in stopWords]
        tags = [word for word in all_words_lowercase if word not in stop_words_lowercase]
        tags = [t[0] for t in Counter(tags).most_common(5)]
        return tags
    
    def validate_file_content(self):
        # would be a good idea to validate the file content
        pass

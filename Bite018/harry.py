import os
import urllib.request
import re
from collections import Counter

# data provided
tmp = os.getenv("TMP", "/tmp")
stopwords_file = os.path.join(tmp, 'stopwords')
harry_text = os.path.join(tmp, 'harry')
urllib.request.urlretrieve(
    'https://bites-data.s3.us-east-2.amazonaws.com/stopwords.txt',
    stopwords_file
)
urllib.request.urlretrieve(
    'https://bites-data.s3.us-east-2.amazonaws.com/harry.txt',
    harry_text
)

with open(stopwords_file) as file:
    stopwords = [line.strip() for line in file]
    
with open(harry_text) as file:
    harry_text = file.read().replace('\n', ' ').lower()
    
def get_harry_most_common_word():
    text = re.sub(r'[^A-Za-z0-9 ]+', '', harry_text)
    words = text.split()
    without_stopwords = [word for word in words if word not in stopwords]
    c = Counter(without_stopwords)
    most_occur = c.most_common(1)
    return most_occur[0]
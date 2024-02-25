import json
import csv
from sklearn.feature_extraction.text import CountVectorizer

file_path = 'data/splits/media/train.tsv'
train = []
labels = []
with open(file_path, mode='r', encoding='utf-8') as file:
    tsv_reader = csv.DictReader(file, delimiter='\t')
    for row in tsv_reader:
        train.append(row["ID"])
        labels.append(row["bias"])


article_name = "sJfVGcfW6vWo04q7"
article_path = f'data/jsons/{article_name}.json' 

with open(article_path, 'r') as file:
    article_json = json.load(file)

print(article_json["authors"])

# Example usage
content = "Your article content here"

##removing stop words from text
with open("data/stop_words_english.json", 'r') as file:
    stop_words_data = json.load(file)
    stop_words_set = set(stop_words_data)

def remove_stop_words(content):
    words = content.split()
    filtered_words = [word for word in words if word not in stop_words_set]
    filtered_content = ' '.join(filtered_words)
    
    return filtered_content








filtered_content = remove_stop_words(content)
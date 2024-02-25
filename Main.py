import json
import csv
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer

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








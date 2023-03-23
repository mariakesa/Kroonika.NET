from bs4 import BeautifulSoup
import codecs
from transformers import BertTokenizer, BertForTokenClassification
from transformers import pipeline
import os
import pandas as pd

# https://stackoverflow.com/questions/70915101/pandas-dataframe-edge-list-to-networkx-graph-object


def process_single_article(article, edge_df):
    chunk_size = 512
    chunks = [article.get_text()[i:i+chunk_size]
              for i in range(0, len(article.get_text()), chunk_size)]
    ner_results = []
    for chunk in chunks:
        chunk_ner_results = nlp(chunk)
        ner_results += chunk_ner_results

    per_names = [entity['word'] for entity in ner_results if entity['entity_group'] == 'PER'
                 and len(entity['word'].split()) >= 2 and '##' not in entity['word']]

    for ne_i in per_names:
        for ne_j in per_names:
            if ne_i != ne_j:
                row = pd.DataFrame({'source': [ne_i], 'target': [ne_j]})
                edge_df = pd.concat([edge_df, row], ignore_index=True)
    return edge_df


def process_single_file(tei_path, edge_df):
    print(tei_path)
    with codecs.open(tei_path, 'r', encoding='ISO 8859-1') as f:
        tei_text = f.read()
        soup = BeautifulSoup(tei_text, 'xml')
        articles = soup.find_all('div2', {'type': 'artikkel'})
        for a in articles:
            edge_df = process_single_article(a, edge_df)
    return edge_df


if __name__ == "__main__":
    tokenizer = BertTokenizer.from_pretrained('tartuNLP/EstBERT_NER')
    bertner = BertForTokenClassification.from_pretrained(
        'tartuNLP/EstBERT_NER')
    nlp = pipeline("ner", model=bertner, tokenizer=tokenizer,
                   aggregation_strategy="simple")

    files = os.listdir('tei')

    edge_df = pd.DataFrame(columns=['source', 'target'])

    for file in files:
        tei_path = 'tei/'+file
        edge_df = process_single_file(tei_path, edge_df)
    edge_df.to_csv('edge_list.csv')

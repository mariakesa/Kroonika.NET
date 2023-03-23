from bs4 import BeautifulSoup
import codecs
from transformers import BertTokenizer, BertForTokenClassification
from transformers import pipeline

tokenizer = BertTokenizer.from_pretrained('tartuNLP/EstBERT_NER')
bertner = BertForTokenClassification.from_pretrained('tartuNLP/EstBERT_NER')

nlp = pipeline("ner", model=bertner, tokenizer=tokenizer,
               aggregation_strategy="simple")


with codecs.open('./tei/kr31.12.2002.tei', 'r', encoding='ISO 8859-1') as f:
    tei_text = f.read()
    soup = BeautifulSoup(tei_text, 'xml')

# Extract the text from the <body> tag
#body_text = soup.body.get_text()

articles = soup.find_all('div2', {'type': 'artikkel'})
# print(articles)

# Print the text
# print(body_text)

#ner_results = nlp(body_text)


# Split the text into chunks of 512 tokens
chunk_size = 512
chunks = [articles[0].get_text()[i:i+chunk_size]
          for i in range(0, len(articles[0].get_text()), chunk_size)]

# Process each chunk separately and combine the results
ner_results = []
for chunk in chunks:
    chunk_ner_results = nlp(chunk)
    #tokens = tokenizer(chunk)
    #tokens = tokenizer.convert_ids_to_tokens(tokens['input_ids'])
    ner_results += chunk_ner_results

# Print the results
for result in ner_results:
    print(result)


# Create an empty list to store the PER class names
per_names = []

per_names = [entity['word'] for entity in ner_results if entity['entity_group']
             == 'PER' and len(entity['word'].split()) >= 2 and '##' not in entity['word']]

# Print the PER class names
# print(per_names)


#tokens = tokenizer(body_text, truncation=True, padding=True, max_length=512)
#tokens = tokenizer.convert_ids_to_tokens(tokens['input_ids'])


#print(f'tokens: {tokens}')
#print(f'NER model:{ner_results}')

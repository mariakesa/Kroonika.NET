from transformers import BertTokenizer, BertForTokenClassification
from transformers import pipeline

tokenizer = BertTokenizer.from_pretrained('tartuNLP/EstBERT_NER')
bertner = BertForTokenClassification.from_pretrained('tartuNLP/EstBERT_NER')

nlp = pipeline("ner", model=bertner, tokenizer=tokenizer,
               grouped_entities=True)

text = "Kaia Kanepi (WTA 57.) langes USA-s Charlestonis toimuval WTA 500 kategooria tenniseturniiril konkurentsist kaheksandikfinaalis, kaotades poolatarile Magda Linette'ile (WTA 64.) 3 : 6, 6 : 4, 2 : 6."

ner_results = nlp(text)

tokens = tokenizer(text)
tokens = tokenizer.convert_ids_to_tokens(tokens['input_ids'])


print(f'tokens: {tokens}')
print(f'NER model:{ner_results}')

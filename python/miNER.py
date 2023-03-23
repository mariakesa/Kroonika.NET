from transformers import pipeline, AutoTokenizer, AutoModelForTokenClassification

tokenizer = AutoTokenizer.from_pretrained("tartuNLP/EstBERT")
model = AutoModelForTokenClassification.from_pretrained("tartuNLP/EstBERT")
recognizer = pipeline("ner", model=model, tokenizer=tokenizer)
print(recognizer('Tere ma olen, Maria! Ma elan Tallinnas.'))

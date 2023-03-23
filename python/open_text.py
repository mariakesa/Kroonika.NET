import xml.etree.ElementTree as ET

# Load the .tei file
#tree = ET.parse('./tei/kr01.04.2003.tei')
# print(tree)
# Get the root element
#root = tree.getroot()
# print(root)

# Find all the text nodes in the document
# text_nodes = root.findall(
# './/{http://www.tei-c.org/ns/1.0}teiHeader//{http://www.tei-c.org/ns/1.0}text//{http://www.tei-c.org/ns/1.0}body//{http://www.tei-c.org/ns/1.0}div//{http://www.tei-c.org/ns/1.0}p//{http://www.tei-c.org/ns/1.0}text()')

# Concatenate the text nodes into a single string
#text = ''.join(text_nodes)

# Print the text content
# print(text)

import codecs
from bs4 import BeautifulSoup

with codecs.open('./tei/kr31.12.2002.tei', 'r', encoding='ISO 8859-1') as f:
    tei_text = f.read()
    soup = BeautifulSoup(tei_text, 'xml')

# Extract the text from the <body> tag
body_text = soup.body.get_text()

# Print the text
print(body_text)

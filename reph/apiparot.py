import requests

import requests
import nltk

from nltk.tokenize import sent_tokenize

API_URL = "https://api-inference.huggingface.co/models/prithivida/parrot_paraphraser_on_T5"
headers = {"Authorization": f"Bearer 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"}

def query(payload):
	response = requests.post(API_URL, headers=headers, json=payload)
	return response.json()

context="""Spider-Man is a superhero appearing in American comic books published by Marvel Comics. Created by writer-editor Stan Lee and artist Steve Ditko, he first appeared in the anthology comic book Amazing Fantasy #15 (August 1962) in the Silver Age of Comic Books. He has been featured in comic books, television shows, films, video games, novels, and plays."""


sentences=nltk.sent_tokenize(context)
array1=[]
array2=[]

print(sentences)
print(len(sentences))



for i in range(0,len(sentences)):
         array1.append(query(sentences[i]))
for i in range(len(array1)):
         array2.append(array1[i][0]['generated_text'])


para=' '.join(array2)
	
output = para

print(output)
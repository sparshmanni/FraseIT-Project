from django.shortcuts import render
from django.http import HttpResponse
import requests
import nltk
nltk.download('punkt')
from nltk.tokenize import sent_tokenize
import time


API_URL = "https://api-inference.huggingface.co/models/prithivida/parrot_paraphraser_on_T5"
headers = {"Authorization": f"Bearer <<key>>"}

def query(payload):
	response = requests.post(API_URL, headers=headers, json=payload)
	return response.json()
	




# Create your views here.
def home(request):
    return render(request,"index.html")

def new(request):
    data = request.GET['thetextarea']
    datta=(data+"    ")
    sentences=nltk.sent_tokenize(datta)
    array1=[]
    array2=[]
    for i in range(0,len(sentences)):
         array1.append(query(sentences[i]))
    for i in array1:
         if i == {'error': 'Model prithivida/parrot_paraphraser_on_T5 is currently loading',
  'estimated_time': 35.669498443603516}:
              time.sleep(5)
              for i in range(0,len(sentences)):
                   array1.append(query(sentences[i]))
    
    
    for i in range(len(array1)):
         array2.append(array1[i][0]['generated_text'])
    
    para=' '.join(array2)
    

    output=para

    return render(request, "next.html", {'output':output,'data':data})

def about(request):
    return render(request,"about.html")

def tryy(request):
    return render(request,"tryy.html")

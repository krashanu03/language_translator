from django.shortcuts import render, HttpResponse
from googletrans import Translator
# Create your views here.

def translator(request):
    
    return render(request,"translator.html")

def translated(request):
    text = request.GET.get('text')
    lang = request.GET.get('lang')
    print('text :', text , 'lang :', lang)
    
    #connect the translator
    translator = Translator()
    
    #detect language
    dt = translator.detect(text)
    dt2 = dt.lang
    
    #translated the text
    translated = translator.translate(text, lang)
    tr  = translated.text
    
    
    return render (request,"translated.html" , {'translated':tr, 'u_lang':dt2, 't_lang':lang })
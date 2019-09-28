from django.http import HttpResponse
from django.shortcuts import render

def homepage(request):
    return render(request,'home.html')

def count(request):
    data = request.GET['fulltextarea']
    word_list = data.split()
    list_length = len(word_list)

    word_dict = {}

    for word in word_list:
        if word in word_dict:
            word_dict[word] += 1
        else:
            word_dict[word] = 1

    return render(request,'count.html',{'fulltext': data , 'words': list_length,'total_words':word_dict.items()})

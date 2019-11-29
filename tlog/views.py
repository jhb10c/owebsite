from django.shortcuts import render
from .models import Post
from django.utils import timezone
from django.shortcuts import render, get_object_or_404





def post_list(request):

    return render(request, 'tlog/post_list.html')


def teaching(request):

    return render(request, 'tlog/teaching.html') 

def research(request):

    return render(request, 'tlog/research.html') 

def dprinting(request):

    return render(request, 'tlog/dprinting.html') 

def news(request):

    return render(request, 'tlog/news.html') 

from django.shortcuts import render
from .models import *

def index(request):
    blog = Blog.objects.order_by("-create_at")[:5]
    tags = 
    return render(request, 'index.html',{'blog':blog})

def article(request):
    return render(request, 'article.html')
from django.shortcuts import render
from blog.models import Article

def home(request):
    Articles=Article.objects.all()
    return render(request,'home/index.html',context={'Articles':Articles})

from django.shortcuts import render
from .models import Blogpost

# Create your views here.

def index(request):
    posts=Blogpost.objects.all()
    return render(request,'blog/index.html',{'post':posts})

def blogpost(request,id):
    postdata=Blogpost.objects.filter(blogid=id)
    return render(request,'blog/blogpost.html',{'pdata':postdata[0]})

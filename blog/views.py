from ast import Pass
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "blog/index.html")

def posts(requset):
    return render(requset, "blog/all-posts.html")

def postDetails():
    pass

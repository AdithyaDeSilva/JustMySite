from ast import Pass
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "blog/index.html")

def posts(requset):
    pass

def postDetails():
    pass

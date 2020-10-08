from django.shortcuts import render

# Create your views here.

def homeView(request):
    return render(request,'index.html',{})


def profileView (request):
    return render(request,'profile.html')

def aboutView (request):
    return render(request, 'about.html')
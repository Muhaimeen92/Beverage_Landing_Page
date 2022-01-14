from django.shortcuts import render
# Create your views here.

def index(request):
    return render(request, "index.html")

def confirmation(request, order_number):
    return render(request, "index.html")
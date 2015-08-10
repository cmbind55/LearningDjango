from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
#def home_page(self):
#    return HttpResponse('')

def home_page(request):
    # View code here... (if any)
    return render(request, 'lists/index.html', {"page_title": "About this site"})
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
#def home_page(self):
#    return HttpResponse('')

def home_page(request):
    return render(request, 'lists/index.html', {
        'new_item_text': request.POST.get('item_text', ''),
        'page_title': 'To-Do',
    })

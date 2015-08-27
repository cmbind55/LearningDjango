from django.shortcuts import redirect, render
from django.http import HttpResponse
from lists.models import Item

#
# Create your views here.
#def home_page(self):
#    return HttpResponse('')

def home_page(request):
    return render(request, 'lists/index.html', {
        'page_title': 'To-Do',
    })

def view_list(request):
    items = Item.objects.all()
    return render(request, 'lists/list.html', {
        'page_title': 'To-Do',
        'items': items,
    })

def new_list(request):
    Item.objects.create(text=request.POST['item_text'])
    return redirect('/lists/the-only-list-in-the-world/', {'page_title': 'To-Do'})

from django.shortcuts import redirect, render
from django.http import HttpResponse
from lists.models import Item

#
# Create your views here.
#def home_page(self):
#    return HttpResponse('')

def home_page(request):
    if request.method == 'POST':
        Item.objects.create(text=request.POST['item_text'])
        return redirect('/lists', {'page_title': 'To-Do'})

    items = Item.objects.all()
    return render(request, 'lists/index.html', {
        'page_title': 'To-Do',
        'items': items,
    })

from django.shortcuts import redirect, render
from django.http import HttpResponse
from lists.models import Item, List
from django.core.exceptions import ValidationError

#
# Create your views here.
#def home_page(self):
#    return HttpResponse('')

def home_page(request):
    return render(request, 'lists/index.html', {
        'page_title': 'To-Do',
    })


def view_list(request, list_id):
    list_ = List.objects.get(id=list_id)
    items = Item.objects.filter(list=list_)
    return render(request, 'lists/list.html', {
        'page_title': 'To-Do',
        'list': list_,
    })


def new_list(request):
    list_ = List.objects.create()
    item = Item.objects.create(text=request.POST['item_text'], list=list_)
    try:
        item.full_clean()
        item.save()
    except ValidationError:
        list_.delete()
        error = "You can't have an empty list item"
        return render(request, 'lists/index.html', {"error": error, 'page_title': 'To-Do'})
    return redirect('/lists/%d/' % (list_.id,), {'page_title': 'To-Do'})


def add_item(request, list_id):
    list_ = List.objects.get(id=list_id)
    Item.objects.create(text=request.POST['item_text'], list=list_)
    return redirect('/lists/%d/' % (list_.id,), {'page_title': 'To-Do'})

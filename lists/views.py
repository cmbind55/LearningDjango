from django.shortcuts import redirect, render
from django.http import HttpResponse
from lists.models import Item, List
from lists.forms import ExistingListItemForm, ItemForm
from django.core.exceptions import ValidationError


#
# Create your views here.
#

def home_page(request):
    return render(request, 'lists/index.html', {'form': ItemForm()})


def new_list(request):
    form = ItemForm(data=request.POST)
    if form.is_valid():
        list_ = List.objects.create()
        form.save(for_list=list_)
        return redirect(list_)
    else:
        return render(request, 'lists/index.html', {"form": form})


def view_list(request, list_id):
    list_ = List.objects.get(id=list_id)
    form = ExistingListItemForm(for_list=list_)
    if request.method == 'POST':
        form = ExistingListItemForm(for_list=list_, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect(list_)
    return render(request, 'lists/list.html', {'list': list_, "form": form})


def my_lists(request, email):
    return render(request, 'lists/my_lists.html')

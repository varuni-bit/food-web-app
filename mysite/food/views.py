from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Item
from .forms import ItemForm
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
# Create your views here.
def index(request):
    #query db
    item_list = Item.objects.all()
    #pass db data to html
    # template = loader.get_template('food/index.html')
    context = {
        'item_list':item_list,
    }
    # return HttpResponse(template.render(context,request))
    return render(request,'food/index.html',context)

#class based view the above one is function based
class IndexClassView(ListView):
    model = Item;
    template_name = 'food/index.html'
    #pass context
    context_object_name = 'item_list'

def item(request):
    return HttpResponse("<h1>this is an item view</h1>")


def detail(request,item_id):
    item = Item.objects.get(pk=item_id)
    context = {
        'item':item,
    }
    return render(request,'food/detail.html',context)

#class based detail view for this import DetailView
class FoodDetail(DetailView):
    model=Item
    template_name = 'food/detail.html'



def create_item(request):
    form = ItemForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('food:index')
    return render(request,'food/item-form.html',{'form':form})

def update_item(request,id):
    item = Item.objects.get(id=id)
    form = ItemForm(request.POST or None, instance=item)

    if form.is_valid():
        form.save()
        return redirect('food:index')
    return render(request, 'food/item-form.html', {'form':form,'item':item})

def delete_item(request,id):
    item = Item.objects.get(id=id)

    if request.method == 'POST':
        item.delete()
        return redirect('food:index')
    return render(request,'food/item-delete.html',{'item':item})
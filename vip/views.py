from .models import Item, Category
from vendor.models import Store
from django.shortcuts import get_object_or_404, render
# from django.db.models import prefetch_related_objects


def index(request):
    item_list = Item.objects.all()
    context = {'item_list': item_list}
    return render(request, 'vip/index.html', context)


def block(request):
    category_list = Category.objects.all()
    store_list = Store.objects.all()
    context = {'store_list':store_list, 'category_list':category_list}
    return render(request, 'vip/block.html', context)

def category (request, category_name):
    item_by_category = Item.objects.filter(category__name = category_name)
    context = {'item_by_category':item_by_category}
    return render(request, 'vip/category.html', context) # render looks into 'templates' folder


def store(request, store_id):
    item_by_store = Item.objects.filter(store__id = store_id)
    context = {'item_by_store':item_by_store}

    return render(request, 'vip/store.html', context)

# def detail(request, item_id):
#     item = get_object_or_404 (Item, pk = item_id)
#     return render(request, 'vip/detail.html', {'item': item})

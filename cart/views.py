from django.shortcuts import render
from .models import Item

# Create your views here.
def show_cart(request): # need consumer_id later

    item_list = Item.objects.filter()

    context = {'item_list':item_list}

    return render(request, 'cart/show_cart.html', context)
from django.shortcuts import render
from vip.models import Item
from cart.models import Order

# Create your views here.
def inventory(request):
    item_list = Item.objects.all()
    context = {'item_list': item_list}
    return render(request, 'vendor/inventory.html', context)

def order(request):
    # take out all orders first
    order_list = Order.objects.all()
    # find item list related to each order

    context = {'order_list': order_list}

    return render(request, 'vendor/order.html', context)

def index(request):
    return render(request, 'vendor/index.html')
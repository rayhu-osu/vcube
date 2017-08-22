from django.shortcuts import render
from vendor.models import Store
from cart.models import Order
from .models import StoreSequence, ConsumerSequence
from vip.models import Item
from sign_up.models import Consumer

# Create your views here.
def index(request, driver_id):

    return render(request, 'valet/index.html', {'driver_id':driver_id})


def availability(request, driver_id):
    #item_list = Item.objects.all()
    context = {'driver_id': driver_id}
    return render(request, 'valet/availabilit2y.html', context)


# order view shows the store sequence
def order(request, driver_id): # oder view based on driver id

    order_num = Order.objects.filter(processed=True).count()
    seq = StoreSequence.objects.get(driver__id=driver_id)
    store_id_list = str(seq).split()
    selected_store = []
    for store_id in store_id_list:
        selected_store.append(Store.objects.get(id=store_id))

    context = {'selected_store': selected_store, 'order_num':order_num, 'driver_id': driver_id}

    return render(request, 'valet/order.html', context)

# store detail shows items in each store
def store_detail(request, driver_id, store_id):

    item_list = Item.objects.filter(store__id=store_id, order__processed=True).distinct()

    context = {'store_id':store_id, 'driver_id': driver_id, 'item_list':item_list}

    return render(request, 'valet/store_detail.html', context)


# deliver shows the consumer sequence
def deliver(request, driver_id):

    order_num = Order.objects.filter(processed=True).count()
    seq = ConsumerSequence.objects.get(driver__id=driver_id)
    consumer_id_list = str(seq).split()

    selected_consumer = []
    for consumer_id in consumer_id_list:
        selected_consumer.append(Consumer.objects.get(id=consumer_id))

    context = {'selected_consumer': selected_consumer, 'order_num':order_num, 'driver_id': driver_id}

    return render(request, 'valet/deliver.html', context)


# shows the orders of each consumer with item detail
def deliver_detail(request, driver_id, consumer_id):
    order_list = Order.objects.filter(consumer__id=consumer_id, processed=True).distinct()

    context = {'order_list':order_list, 'driver_id': driver_id, 'consumer_id':consumer_id}

    return render(request, 'valet/deliver_detail.html', context)


from django.shortcuts import render
from vip.models import Item

def index (request):

    item_list = Item.objects.filter()
    context = {'item_list': item_list}

    return render(request, 'crowdshipping/home.html', context) # render looks into 'templates' folder


def contact(request):
    return render (request, 'crowdshipping/basic.html',
	{'contactinfo': ["If you'd like to contact us, please email to Ray Hu: ruihu.osu@gmail.com"]})
    # render takes 3 parameters (request, what you want to render (the html), dictionary)
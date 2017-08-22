from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = 'vendor'
urlpatterns = [

	url(r'^$', views.index, name='index'),
	url(r'^inventory/$', views.inventory, name='inventory'),
	url(r'^order/$', views.order, name='order'),

    # ex: /vip/ this is the home page
    # url(r'^$', views.inventory, name='index'),
    # ex: /vip/item&5/, this is the detail of the page
    # url(r'^(?P<category_name>[a-zA-Z_]*)/$', views.item, name='item'),
    # url(r'^(?P<item_id>[0-9]+)/$', views.detail, name='detail'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
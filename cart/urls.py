from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static

from . import views

app_name = 'cart'
urlpatterns = [
    # ex: /vip/ this is the home page
    url(r'^$', views.show_cart, name='show_cart'),
    # ex: /vip/item&5/, this is the detail of the page
    # url(r'^(?P<category_name>[a-zA-Z_]*)/$', views.item, name='item'),
    # url(r'^(?P<item_id>[0-9]+)/$', views.detail, name='detail'),
    # ex: /vip/5/results/
    # url(r'^(?P<number_id2>[0-9]+)/results/$', views.results, name='results'),
    # ex: /demo/5/vote/
    #url(r'^(?P<number_id>[0-9]+)/vote/$', views.vote, name='vote'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
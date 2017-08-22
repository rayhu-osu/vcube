from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static

from . import views

app_name = 'vip'
urlpatterns = [

    url(r'^$', views.block, name='block'),
    url(r'^index/$', views.index, name='index'),
    url(r'^(?P<category_name>[a-zA-Z\s]*)/$', views.category, name='category'),
    url(r'^(?P<store_id>[0-9]+)/$', views.store, name='store'),
    url(r'^(?P<item_id>[0-9]+)/$', views.detail, name='detail'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = 'valet'
urlpatterns = [
	url(r'^(?P<driver_id>[0-9]+)/$', views.index, name='index'),
	url(r'^(?P<driver_id>[0-9]+)/availability/$', views.availability, name='availability'),
	url(r'^(?P<driver_id>[0-9]+)/order/$', views.order, name='order'),
	url(r'^(?P<driver_id>[0-9]+)/order/(?P<store_id>[0-9]+)/$', views.store_detail, name='store_detail'),
	url(r'^(?P<driver_id>[0-9]+)/deliver/$', views.deliver, name='deliver'),
	url(r'^(?P<driver_id>[0-9]+)/deliver/(?P<consumer_id>[0-9]+)/$', views.deliver_detail, name='deliver_detail'),



] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
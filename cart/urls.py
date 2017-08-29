from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static

from . import views

app_name = 'cart'
urlpatterns = [
    # ex: /vip/ this is the home page
    url(r'^$', views.show_cart, name='show_cart'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
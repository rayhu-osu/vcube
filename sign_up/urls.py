from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static

from . import views

app_name = 'sign_up'
urlpatterns = [

    url(r'^$', views.register, name='register'),
    url(r'^consumer/$', views.consumer, name='consumer'),
    url(r'^store/$', views.store, name='store'),
    url(r'^driver$', views.driver, name='driver'),
    url(r'^login/$', views.login, name='login'),
    # url(r'^redirect/$', views.redirect, name='redirect'),
    url(r'^success/$', views.success, name='success'),
    url(r'^success/thanks/$', views.thanks, name='thanks'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
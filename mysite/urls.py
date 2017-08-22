"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
        url(r'^admin/', admin.site.urls),
        url(r'^', include('crowdshipping.urls')),
        url(r'^blog/', include('blog.urls')),
        url(r'^demo/', include('demo.urls')),
        url(r'^vip/', include('vip.urls')),
        url(r'^copydata/', include('copydata.urls')),
        url(r'^sign_up/', include('sign_up.urls')),
        url(r'^cart/', include('cart.urls')),
        url(r'^valet/', include('valet.urls')),
        url(r'^vendor/', include('vendor.urls')),
]

# if settings.DEBUG is True:
# 	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

from django.conf.urls import url, include
from django.views.generic import ListView, DetailView
from blog.models import Post


urlpatterns = [
	url(r'^$', ListView.as_view(queryset = Post.objects.all().order_by("-date")[:25],
	template_name = "blog/blog.html")),
	# queryset object here: https://docs.djangoproject.com/en/1.11/ref/models/querysets/
	url(r'^(?P<pk>\d+)$', DetailView.as_view(model = Post, template_name = 'blog/post.html')) # pk stands for primary-key in the database
	]
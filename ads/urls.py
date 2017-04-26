from django.conf.urls import include, url
from django.contrib import admin

from bakery import views

urlpatterns = [
	# url(r'^$', views.index, name="index"),
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.post_list, name='post_list'),
]
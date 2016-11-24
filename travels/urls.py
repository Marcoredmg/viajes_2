from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.hello_world, name='hello'),
	url(r'^travel/(?P<pk>[0-9]+)/$', views.travel_detail),
	url(r'^travel/new', views.new_travel, name="new_travel")
]
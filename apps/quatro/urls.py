from django.conf.urls import url
from . import views           
urlpatterns = [
	url(r'^$', views.index),
	url(r'^register$', views.register),
	url(r'^login$', views.login),
	url(r'^logout$', views.logout),
	url(r'^home$', views.home),
	url(r'^add/(?P<id>\d+)$', views.add),
	url(r'^profile/(?P<id>\d+)$', views.profile),
	url(r'^remove/(?P<id>\d+)$', views.remove),

]
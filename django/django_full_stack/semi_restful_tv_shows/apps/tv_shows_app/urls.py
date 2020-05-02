from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.shows),
    url(r'^shows$', views.shows),
    url(r'^shows/new$', views.add_show),
    url(r'^shows/create_show', views.create_show),
    url(r'^shows/(?P<newShow_id>\d+)$', views.new_show),
    url(r'^shows/(?P<newShow_id>\d+)/edit_show$', views.edit_show),
    url(r'^shows/(?P<newShow_id>\d+)/update_show$', views.update_show),
    url(r'^shows/(?P<newShow_id>\d+)/destroy$', views.delete),
]
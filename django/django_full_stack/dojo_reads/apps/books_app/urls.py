from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^login$', views.login),
    url(r'^register$', views.register),
    url(r'^logout$', views.logout),
    url(r'^home', views.home),
    url(r'^add_book_and_review$', views.add_book_and_review),
    url(r'^book/(?P<book_id>\d+)$', views.book),
 
]
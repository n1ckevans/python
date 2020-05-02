from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^add_book$', views.add_book),
    url(r'^books/(?P<book_id>\d+)$', views.book),
    url(r'^authors$', views.all_authors),
    url(r'^authors/(?P<auth_id>\d+)$', views.author),
    url(r'^authors/add_author$', views.add_author),
]
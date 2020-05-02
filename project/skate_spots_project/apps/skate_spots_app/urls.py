from django.conf.urls import url
# from . import settings
from . import views




urlpatterns = [
    url(r'^$', views.index),
    url(r'^login$', views.login),
    url(r'^register$', views.register),
    url(r'^logout$', views.logout),
    url(r'^home$', views.home),
    url(r'^wall$', views.wall),
    url(r'^add_message$', views.add_message),
    url(r'^add_comment/$', views.add_comment),
    url(r'^delete/(?P<message_id>\d+)$', views.delete),
    url(r'^message/(?P<message_id>\d+)$', views.message),
    url(r'^profile/(?P<user_id>\d+)$', views.profile),
    url(r'^update/(?P<user_id>\d+)$', views.profile),
    # url(r'^site_media/(.*)$', 'django.views.static.serve', {'document_root' : settings.MEDIA_ROOT}),
]
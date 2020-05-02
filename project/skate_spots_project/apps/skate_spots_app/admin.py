from django.contrib import admin

from .models import User, Message, Comment, Marker

admin.site.register(User)
admin.site.register(Message)
admin.site.register(Comment)
admin.site.register(Marker)
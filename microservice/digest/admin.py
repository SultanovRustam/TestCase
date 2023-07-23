from django.contrib import admin

from .models import Digest, Post, Source, Subscription, User

admin.site.register(Digest)
admin.site.register(Post)
admin.site.register(Source)
admin.site.register(Subscription)
admin.site.register(User)

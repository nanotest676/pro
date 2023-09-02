from django.contrib import admin

from .models import Post, Category, Location, User


admin.site.register(Post)
admin.site.register(Category)
admin.site.register(Location)

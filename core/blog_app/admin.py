from django.contrib import admin
from blog_app.models import Category, Post


class PostAdmin(admin.ModelAdmin):
    list_display = ['author', 'title', 'status', 'created_date', 'published_date']


admin.site.register(Category)
admin.site.register(Post, PostAdmin)
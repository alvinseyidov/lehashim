from django.contrib import admin
from .models import *

admin.site.register(Blog)
admin.site.register(Tag)


@admin.register(BlogCategory)
class BlogCategoryAdmin(admin.ModelAdmin):
    model = BlogCategory
    list_display = ['name','parent']
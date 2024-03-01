from django.contrib import admin
from .models import *

from django.contrib import admin
from mptt.admin import DraggableMPTTAdmin
from django_mptt_admin.admin import DjangoMpttAdmin

class CountryAdmin(DjangoMpttAdmin):
    pass

admin.site.register(Category, DraggableMPTTAdmin,
                    list_display=(
                        'tree_actions',
                        'indented_title',
                        # ...more fields if you feel like it...
                    ),
                    list_display_links=(
                        'indented_title',
                    ),
                    )



@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ['title','cat','publish_datetime','views']
    search_fields = ['title','cat',]

admin.site.register(SelectedBlog)
admin.site.register(Review)

admin.site.register(Tag)



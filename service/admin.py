from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import *


class ServiceAdmin(SummernoteModelAdmin):
    summernote_fields = '__all__'

admin.site.register(Service, ServiceAdmin)
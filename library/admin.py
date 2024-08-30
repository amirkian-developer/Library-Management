from django.contrib import admin
from .models import *

@admin.register(Book)
class TraderAdmin(admin.ModelAdmin):
    list_display = [f.name for f in Book._meta.fields]

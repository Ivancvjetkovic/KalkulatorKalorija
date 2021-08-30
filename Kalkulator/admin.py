from django.contrib import admin
from .models import *

# Register your models here.

class foodAdmin(admin.ModelAdmin):
    class Meta:
        model=Namirnica
    list_display=['naziv']
    list_filter=['naziv']

admin.site.register(Tabla)
admin.site.register(RelacijaTablaNamirnica)
admin.site.register(Namirnica,foodAdmin)


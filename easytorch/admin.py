from django.contrib import admin
from .models import Easy

class EasyAdmin(admin.ModelAdmin):
    list_display = ('type','neurons','layers_neurons')

admin.site.register(Easy,EasyAdmin)

# Register your models here.

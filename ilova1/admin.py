from django.contrib import admin
from .models import Meva
class MevaAdmin(admin.ModelAdmin):
    list_display = ('title','desc','price')
# Register your models here.
admin.site.register(Meva,MevaAdmin)
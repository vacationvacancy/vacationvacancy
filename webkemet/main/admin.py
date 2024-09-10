from django.contrib import admin
from .models import Figure


@admin.register(Figure)
class FigureAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name',)  


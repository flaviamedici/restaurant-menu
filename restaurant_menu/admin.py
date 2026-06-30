from django.contrib import admin
from .models import Item

class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('dish', 'status')
    list_filter = ('status',)
    search_fields = ('dish', 'description')

admin.site.register(Item, MenuItemAdmin)
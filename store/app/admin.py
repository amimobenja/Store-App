from django.contrib import admin
from app.models import Category, Item, UserProfile

class CategoryAdmin(admin.ModelAdmin):
	list_display = ('name',)
	
class ItemAdmin(admin.ModelAdmin):
	list_display = ('category', 'item_name', 'item_description', 'price', 'address')

admin.site.register(Category, CategoryAdmin)
admin.site.register(Item, ItemAdmin)
admin.site.register(UserProfile)

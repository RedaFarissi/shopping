from django.contrib import admin
from .models import Category , Product , Like ,  Size

admin.site.register(Size)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}
admin.site.register(Category, CategoryAdmin)

class ProductAdmin(admin.ModelAdmin):
    list_display = ['user','name', 'slug', 'price','available', 'created', 'updated']
    prepopulated_fields = {'slug': ('name',)}
    list_editable = ['price', 'available']
    list_filter = ['available', 'created', 'updated']
admin.site.register(Product, ProductAdmin)
    
class LikeAdmin(admin.ModelAdmin):
    list_display = ['user', 'product']
admin.site.register(Like, LikeAdmin)
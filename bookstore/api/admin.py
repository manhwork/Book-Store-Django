from django.contrib import admin
from django.utils.html import format_html
from .models import Product, Category

# Register your models here.

# class CategoryAdmin(admin.ModelAdmin):
#     list_display = ('image_tag', 'title', 'created_at', 'updated_at','slug')
    # search_fields = ('title', 'description')
    # prepopulated_fields = {'slug': ('title',)}
    # list_filter = ["title"]

    # def image_tag(self, obj):
    #     if obj.image:
    #         return format_html('<img src="./media/category/Capturehiu.PNG" width="50" height="50" />')
    #     return '-'
    # image_tag.short_description = 'Image'

# class ProductAdmin(admin.ModelAdmin):
#     list_display = ('title', 'price', 'discount', 'quantity', 'created_at', 'updated_at','slug')
#     search_fields = ('title', 'description')
#     list_filter = ('title','price')
#     prepopulated_fields = {'slug': ('title',)}

# admin.site.register(Product, ProductAdmin)
# admin.site.register(Category, CategoryAdmin)

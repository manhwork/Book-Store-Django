from django.contrib import admin
from django.utils.html import format_html
from.models import *


@admin.action(description="Mark selected categories as active")
def make_active(modeladmin, request, queryset):
    queryset.update(isActive=True)

@admin.action(description="Mark selected categories as inactive")
def make_inactive(modeladmin, request, queryset):
    queryset.update(isActive=False)

# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    list_display = ("image_tag", "title", "isActive", "slug")
    prepopulated_fields = {"slug": ("title",)}
    search_fields = ["title"]
    list_filter = ["isActive"]
    actions = [make_active, make_inactive]


class BookAdmin(admin.ModelAdmin):
    list_display = ("image","Category","Author","title","price","discountPer","stock",  "isActive","isOutStanding")
    prepopulated_fields = {"slug": ("title",)}
    search_fields = ["title"]
    list_filter = ["isActive"]
    actions = [make_active, make_inactive]

    


admin.site.register(Book,BookAdmin)
admin.site.register(Category,CategoryAdmin)
admin.site.register(Blog)
admin.site.register(CategoryBlog)
admin.site.register(Author)
admin.site.register(Review)
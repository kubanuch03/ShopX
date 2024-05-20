from django.contrib import admin
from .models import Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'parent',
        'slug'
    )
    ordering = ('name',)

    def get_prepopulated_fields(self, request, obj=None): # autofill in admin
        return {
            'slug': ('name',),
        }


# @admin.register(Category)
# class CategoryAdmin(admin.ModelAdmin):
#     list_display = ["id", "name", "slug", "img"]
#     prepopulated_fields = {"slug": ("name",)}
#     search_fields = ["name"]
#

# @admin.register(PodCategory)
# class PodCategory(admin.ModelAdmin):
#     list_display = ["id", "name", "slug"]
#     prepopulated_fields = {"slug": ("name",)}
#     search_fields = ["name"]
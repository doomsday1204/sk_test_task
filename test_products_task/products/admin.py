from django.contrib import admin

from products.models import Category, Product, Like


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'slug',
        'price',
        'description',
        'category',
        'image',
    )


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'slug',
    )
    readonly_fields = ('slug',)


@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    pass

from django.contrib import admin

from shoping.models import Category, Product

# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name",)



@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "price_for_one", "category",)
    list_filter = ("category",)
    search_fields = ("name", "description")

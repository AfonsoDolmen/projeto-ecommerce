from django.contrib import admin
from products.models import Product, Category


class ProductAdmin(admin.ModelAdmin):
    class Meta:
        list_display = ('title', 'description', 'price')
        search_fields = ('title', 'description')
        list_filter = ('price')


class CategoryAdmin(admin.ModelAdmin):
    class Meta:
        list_display = ('category')
        search_fields = ('category')


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)

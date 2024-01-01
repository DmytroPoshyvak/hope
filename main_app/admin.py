from django.contrib import admin
from main_app.models import *

class PhotoLine(admin.TabularInline):
    model = Photos
    extra = 0

class ProductsInOrderLine(admin.TabularInline):
    model = ProductInOrder
    extra = 0

class ProductAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Product._meta.fields]
    list_editable = ['name' , 'slug' , 'is_active' , 'is_new']
    inlines = [PhotoLine]

    class Meta:
        model = Product

class CategoryAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Category._meta.fields]
    list_editable = ['category' , 'slug' , 'is_active']
    list_filter = ['id']
    list_display_links = ['id']

    class Meta:
        model = Category

class PhotosAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Photos._meta.fields]

    class Meta:
        model = Photos

class ProdcutInBasketAdmin(admin.ModelAdmin):
    list_display = [field.name for field in ProductInBasket._meta.fields]
    class Meta:
        model = ProductInBasket

class OrderAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Order._meta.fields]
    inlines = [ProductsInOrderLine]
    class Meta:
        model = Order

class ProductInOrderAdmin(admin.ModelAdmin):
    list_display = [field.name for field in ProductInOrder._meta.fields]
    class Meta:
        model = ProductInOrder
    

admin.site.register(Product , ProductAdmin)
admin.site.register(Category , CategoryAdmin)
admin.site.register(Photos , PhotosAdmin)
admin.site.register(ProductInBasket , ProdcutInBasketAdmin)
admin.site.register(Order , OrderAdmin)
admin.site.register(ProductInOrder , ProductInOrderAdmin)
admin.site.register(Status)
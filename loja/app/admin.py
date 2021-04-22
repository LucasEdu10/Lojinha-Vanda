from django.contrib import admin
from .models import Product, ProductType, Fabric


class ProductAdmin(admin.ModelAdmin):
    list_display=('name_product', 'available_product')

class ProductTypeAdmin(admin.ModelAdmin):
    list_display=('name_product',)

class FabricAdmin(admin.ModelAdmin):
    list_display=('cod_fabric','name_fabric', 'type_fabric', 'available_fabric')

    
admin.site.register(Product, ProductAdmin)
admin.site.register(ProductType, ProductTypeAdmin)
admin.site.register(Fabric, FabricAdmin)
# Register your models here.

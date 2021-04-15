from django.contrib import admin
from .models import Fabric


class FabricAdmin(admin.ModelAdmin):
    list_display=('name_fabric', 'available_fabric')
    

    
admin.site.register(Fabric, FabricAdmin)
# Register your models here.

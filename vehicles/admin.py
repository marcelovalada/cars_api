from django.contrib import admin
from .models import Vehicle, VehicleType

# Register your models here.
@admin.register(Vehicle)
class VehicleAdmin(admin.ModelAdmin):
    list_display = ('license_plate', 'brand', 'model', 'color', 'created_at', 'updated_at')
    list_filter = ('license_plate',)
    search_fields = ('license_plate', 'model')

@admin.register(VehicleType)
class VehicleTypeAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'created_at', 'updated_at')
    search_fields = ('name',)
    
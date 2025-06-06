from django.contrib import admin
from .models import ParkingSpot, ParkingRecord

# Register your models here.
@admin.register(ParkingSpot)
class ParkingSpotAdmin(admin.ModelAdmin):
    list_display = ('spot_number', 'is_occupied', 'created_at', 'updated_at')
    list_filter = ('is_occupied',)
    search_fields = ('spot_number',)

@admin.register(ParkingRecord)
class ParkingRecordAdmin(admin.ModelAdmin):
    list_display = ('vehicle', 'parking_spot', 'entry_time', 'exit_time', 'created_at', 'updated_at')
    search_fields = ('vehicle__license_plate', 'parking_spot__spot_number')

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        from .models import ParkingRecord
        if db_field.name == 'parking_spot':
            qs = ParkingSpot.objects.filter(is_occupied=False)
            if request.resolver_match and request.resolver_match.kwargs.get('object_id'):
                try:
                    obj_id = request.resolver_match.kwargs.get('object_id')
                    record = ParkingRecord.objects.get(pk=obj_id)
                    qs = ParkingSpot.objects.filter(is_occupied=False) | ParkingSpot.objects.filter(pk=record.parking_spot.pk)
                except Exception:
                    pass
            kwargs["queryset"] = qs.distinct()
        elif db_field.name == 'vehicle':
            # Veículos que NÃO estão com ParkingRecord ativo (exit_time is None)
            from vehicles.models import Vehicle
            vehicles_with_active_parking = ParkingRecord.objects.filter(exit_time__isnull=True).values_list('vehicle_id', flat=True)
            qs = Vehicle.objects.exclude(id__in=vehicles_with_active_parking)
            if request.resolver_match and request.resolver_match.kwargs.get('object_id'):
                try:
                    obj_id = request.resolver_match.kwargs.get('object_id')
                    record = ParkingRecord.objects.get(pk=obj_id)
                    qs = qs | Vehicle.objects.filter(pk=record.vehicle.pk)
                except Exception:
                    pass
            kwargs["queryset"] = qs.distinct()
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


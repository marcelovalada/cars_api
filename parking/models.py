from django.db import models
from vehicles.models import Vehicle

# Create your models here.
class ParkingSpot(models.Model):
    spot_number = models.CharField(max_length=10, unique=True)
    is_occupied = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Estacionamento'
        verbose_name_plural = 'Estacionamentos'

    def __str__(self):
        return self.spot_number

class ParkingRecord(models.Model):
    vehicle = models.ForeignKey('vehicles.Vehicle', on_delete=models.PROTECT, related_name='parking_records')
    parking_spot = models.ForeignKey(ParkingSpot, on_delete=models.PROTECT, related_name='parking_records')
    entry_time = models.DateTimeField(auto_now_add=True)
    exit_time = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Registro de Estacionamento'
        verbose_name_plural = 'Registros de Estacionamento'

    def __str__(self):
        return f'{self.vehicle} - {self.parking_spot}'
    
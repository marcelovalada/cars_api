from django.db import models
from customers.models import Customer

# Create your models here.
class VehicleType(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Tipo de Veículo'
        verbose_name_plural = 'Tipos de Veículos'

    def __str__(self):
        return self.name

class Vehicle(models.Model):
    vehicle_type = models.ForeignKey(VehicleType, on_delete=models.PROTECT, blank=True, null=True)
    owner = models.ForeignKey(Customer, on_delete=models.PROTECT, blank=True, null=True, related_name='vehicles', verbose_name='Proprietário')
    license_plate = models.CharField(max_length=10, unique=True)
    brand = models.CharField(max_length=100, blank=True, null=True)
    year = models.IntegerField()
    color = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Veículo'
        verbose_name_plural = 'Veículos'

    def __str__(self):
        return self.license_plate
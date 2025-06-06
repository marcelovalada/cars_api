from django.contrib import admin
from .models import Customer

# Register your models here.

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('name', 'cpf', 'phone', 'created_at', 'updated_at')
    search_fields = ('name', 'cpf', 'phone')
from django.db import models
from django.utils import timezone

class Warehouse(models.Model):
    name = models.CharField(max_length=100)
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)

    def __str__(self):
        return self.name

class Agent(models.Model):
    name = models.CharField(max_length=100)
    warehouse = models.ForeignKey(Warehouse, on_delete=models.CASCADE, related_name='agents')
    max_work_hours = models.PositiveIntegerField(default=10)   # hours per day
    max_distance_km = models.PositiveIntegerField(default=100) # km per day

    def __str__(self):
        return f"{self.name} (@{self.warehouse.name})"

class Order(models.Model):
    warehouse = models.ForeignKey(Warehouse, on_delete=models.CASCADE, related_name='orders')
    address = models.TextField()
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    distance_km = models.FloatField(help_text='Distance from warehouse')
    assigned = models.BooleanField(default=False)
    assigned_agent = models.ForeignKey(Agent, on_delete=models.SET_NULL, null=True, blank=True, related_name='orders')
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Order #{self.id} @ {self.address[:20]}"
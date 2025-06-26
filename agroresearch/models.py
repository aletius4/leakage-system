from django.db import models
from django.conf import settings

class LeakReport(models.Model):
    LEAK_TYPE_CHOICES = [
        ('Uvujaji kwenye bomba kuu', 'Main pipe leakage'),
        ('Uvujaji kwenye mita ya maji', 'Meter leakage'),
        ('pipe bursting', 'bomba limepasuka'),
        ('Uvujaji kutoka kwenye joint', 'Valve/joint leakage'),
        ('Others', 'Nyingine'),
    ]

    customer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    leak_type = models.CharField(max_length=50, choices=LEAK_TYPE_CHOICES)
    description = models.TextField(blank=True, null=True)  # Optional description
    latitude = models.FloatField(null=True, blank=True)     # Ruhusu null, itakusaidia error handling
    longitude = models.FloatField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Leak of {self.customer.username} - {self.get_leak_type_display()}"

    class Meta:
        ordering = ['-created_at']  # Onyesha mpya kwanza

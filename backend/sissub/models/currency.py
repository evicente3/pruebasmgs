from django.db import models
from django.core.exceptions import ValidationError

def validar_codigo_moneda(value):
    if len(value) != 3 or not value.isupper():
        raise ValidationError("El código de la moneda debe tener exactamente 3 letras mayúsculas (Ej: USD, PEN).")

class Currency(models.Model):
    id = models.CharField(primary_key=True, max_length=3, validators=[validar_codigo_moneda])
    symbol = models.CharField(max_length=5)
    status = models.CharField(max_length=20, default='Active')
    
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    created_id = models.UUIDField(null=True, blank=True)
    modified_id = models.UUIDField(null=True, blank=True)

    class Meta:
        managed = False
        db_table = 'currencies'

    def __str__(self):
        return f"Moneda: {self.symbol} ({self.id})"

    def save(self, *args, **kwargs):
        if self.symbol:
            self.symbol = self.symbol.upper().strip()
        self.full_clean()
        super().save(*args, **kwargs)

from django.db import models
from django.core.exceptions import ValidationError
from datetime import date

def validar_monto_positivo(value):
    if value <= 0:
        raise ValidationError("El monto de suscripción debe ser estrictamente mayor a cero.")

def validar_fecha_futura(value):
    if value and value < date.today():
        raise ValidationError("La próxima fecha de facturación no puede ser en el pasado.")

class Subscription(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey('sissub.UserProfile', on_delete=models.CASCADE, db_column='user_id')
    service = models.ForeignKey('sissub.Service', on_delete=models.DO_NOTHING, db_column='service_id')
    category = models.ForeignKey('sissub.Category', on_delete=models.SET_NULL, null=True, blank=True, db_column='category_id')
    currency = models.ForeignKey('sissub.Currency', on_delete=models.DO_NOTHING, db_column='currency_id')
    
    amount = models.DecimalField(max_digits=10, decimal_places=2, validators=[validar_monto_positivo])
    billing_cycle = models.CharField(max_length=50, db_column='billingcycle')
    next_billing_date = models.DateField(db_column='nextbillingdate', validators=[validar_fecha_futura])
    status = models.CharField(max_length=20, default='Active')
    
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    created_id = models.UUIDField(null=True, blank=True)
    modified_id = models.UUIDField(null=True, blank=True)

    class Meta:
        managed = False
        db_table = 'subscriptions'

    def __str__(self):
        return f"Suscripción {self.id}: {self.service.name} - {self.amount} {self.currency.id}"

    def save(self, *args, **kwargs):
        if self.billing_cycle:
            self.billing_cycle = self.billing_cycle.lower().strip()
        self.full_clean()
        super().save(*args, **kwargs)

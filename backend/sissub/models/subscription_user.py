from django.db import models
from django.core.exceptions import ValidationError

def validar_porcentaje(value):
    if value <= 0 or value > 100:
        raise ValidationError("El porcentaje debe estar en el rango de 0.01 a 100.00.")

class SubscriptionUser(models.Model):
    id = models.AutoField(primary_key=True)
    subscription = models.ForeignKey('sissub.Subscription', on_delete=models.CASCADE, db_column='subscription_id')
    user = models.ForeignKey('sissub.UserProfile', on_delete=models.CASCADE, db_column='user_id')
    percentage = models.DecimalField(max_digits=5, decimal_places=2, validators=[validar_porcentaje])
    status = models.CharField(max_length=20, default='Active')
    
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    created_id = models.UUIDField(null=True, blank=True)
    modified_id = models.UUIDField(null=True, blank=True)

    class Meta:
        managed = False
        db_table = 'subscriptions_users'

    def __str__(self):
        return f"{self.user.username} asume {self.percentage}% de Suscripción {self.subscription.id}"

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)

from django.db import models
from django.core.exceptions import ValidationError

def validar_nombre(value):
    if len(value.strip()) < 3:
        raise ValidationError("El nombre debe contener al menos 3 caracteres.")

class Service(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, validators=[validar_nombre])
    is_custom = models.BooleanField(default=False, db_column='iscustom') # Postgres convierte a minúsculas
    status = models.CharField(max_length=20, default='Active')
    
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    created_id = models.UUIDField(null=True, blank=True)
    modified_id = models.UUIDField(null=True, blank=True)

    class Meta:
        managed = False 
        db_table = 'services'

    def __str__(self):
        return f"Servicio: {self.name} [{self.status}]"

    def save(self, *args, **kwargs):
        if self.name:
            self.name = self.name.strip()
        
        self.full_clean()
        super().save(*args, **kwargs)

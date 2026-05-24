import uuid
from django.db import models
from django.core.exceptions import ValidationError

# Función de restricción 
def validar_correo(value):
    if not value.endswith(".com") and not value.endswith(".edu.pe"):
        raise ValidationError("El correo debe tener un dominio válido (.com o .edu.pe).")
    if "@" not in value or len(value) < 5:
        raise ValidationError("El formato del correo electrónico es inválido.")

class UserProfile(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(max_length=255, unique=True, validators=[validar_correo])
    username = models.CharField(max_length=100, null=True, blank=True)
    status = models.CharField(max_length=20, default='Active')
    
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    created_id = models.UUIDField(null=True, blank=True)
    modified_id = models.UUIDField(null=True, blank=True)

    class Meta:
        managed = False       
        db_table = 'users'    

    def __str__(self):
        return f"{self.username} ({self.email}) - Estado: {self.status}"

    def save(self, *args, **kwargs):
        # Asegurar que el nombre de usuario siempre se guarde en minúsculas
        if self.username:
            self.username = self.username.lower().strip()
            
        # Fuerza la ejecución de los validadores 
        self.full_clean()
        
        super().save(*args, **kwargs)

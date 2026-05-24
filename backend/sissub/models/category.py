from django.db import models

class Category(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey('sissub.UserProfile', on_delete=models.CASCADE, db_column='user_id')
    name = models.CharField(max_length=100)
    status = models.CharField(max_length=20, default='Active')
    
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    created_id = models.UUIDField(null=True, blank=True)
    modified_id = models.UUIDField(null=True, blank=True)

    class Meta:
        managed = False
        db_table = 'categories'

    def __str__(self):
        return f"Categoría: {self.name}"

    def save(self, *args, **kwargs):
        if self.name:
            self.name = self.name.capitalize().strip()
        self.full_clean()
        super().save(*args, **kwargs)

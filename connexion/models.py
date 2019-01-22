from django.db import models
from django.utils import timezone

# Create your models here.
class User(models.Model):
    id = models.AutoField(primary_key=True)
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    mail = models.CharField(max_length=100)
    fonction = models.CharField(max_length=60)
    pass1 = models.CharField(max_length=100)
    pass2 = models.CharField(max_length=100)
    date = models.DateTimeField(default=timezone.now, verbose_name="Date de parution")

    class Meta:
        ordering = ['date']
        
    def __str__(self):
        return self.mail
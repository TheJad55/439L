from django.db import models
class Contact(models.Model):
    
    
    name = models.CharField(max_length=255)
    address = models.TextField()
    profession = models.CharField(max_length=255)
    telnumber = models.CharField(max_length=20)
    email_address = models.EmailField()
    age = models.PositiveIntegerField(default=1)
    marital_status = models.CharField(max_length=1, default='s')

    def __str__(self):
        return self.name

# Create your models here.

from django.db import models

# Create your models here.
class device(models.Model):
    name = models.CharField(max_length=100)
    status = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
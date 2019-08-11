from django.db import models

# Create your models here.

class SUser(model.Model):
    eamil = models.EmailField()
    password = models.CharField(max_length=64)
    register_date = models.DateTimeField(auto_now_add=True);
    
    
    
from distutils.command.upload import upload
from email import message
from pyexpat import model
from django.db import models

# Create your models here.
class query(models.Model):
    email = models.EmailField()
    Msg = models.CharField(max_length=300)
    
SELECT_CATEGORY = (
    ('l','laptop'),('c','console'),('d','desktop')
)
    
class material(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()
    desc = models.CharField(max_length=500)
    img = models.ImageField(upload_to="static/images")
    category = models.CharField(choices=SELECT_CATEGORY,max_length=500)

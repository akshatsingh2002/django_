from distutils.command.upload import upload
from email import message
from pyexpat import model
from django.db import models
from django.contrib.auth.models import User
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
    
class Cart(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,default=1)
    product=models.ForeignKey(material,on_delete=models.CASCADE)
    quantity=models.PositiveIntegerField(default=1)

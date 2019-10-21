from django.db import models
from datetime import datetime
class Realtor(models.Model):
    name = models.CharField(max_length=200)
    photo = models.ImageField(upload_to='photos/%y/%m/%d/')
    description = models.TextField(blank=True, null=True)
    email = models.EmailField(max_length=254)
    phone = models.IntegerField()
    is_mvp = models.BooleanField(default=False)
    hire_date = models.DateTimeField(default = datetime.now,blank=True)
    

    def __str__(self):
         return self.name

   

from django.db import models


class Customer(models.Model):
    name = models.CharField(max_length=26)
    adress = models.CharField(max_length=26)
    age = models.IntegerField()
    
    def __str__(self):
        return self.name
    

   
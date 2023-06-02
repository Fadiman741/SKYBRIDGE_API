from django.db import models

# Create your models here.
class Property(models.Model):
        name=models.CharField( max_length=100)
        image=models.CharField(max_length=100)
        type=models.CharField(max_length=20)
        province=models.CharField(max_length=20)
        address=models.CharField(max_length=100)
        description=models.CharField(max_length=300)
        # name=models.CharField()
        dateListed =models.DateField()
        rooms=models.IntegerField()
        bathrooms=models.IntegerField()
        garage=models.IntegerField()
        size=models.IntegerField()
        price=models.IntegerField()

        def __str__(self):
                return self.name

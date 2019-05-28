from django.db import models


# Create your models here.


class Staff(models.Model):
    name=models.CharField(max_length=30)
    surname=models.CharField(max_length=30)
    age=models.CharField(max_length=10)
    staff_picture=models.ImageField(upload_to='uploaded_images',null=True, blank=True)
    staff_id=models.CharField(max_length=30,null=True, blank=True)
    staff_post=models.CharField(max_length=30,null=True, blank=True)
    def __str__(self):
        return self.name
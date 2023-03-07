from django.db import models
from django.db import models
 
class Login(models.Model):
    fname=models.CharField(max_length=20)
    lname=models.CharField(max_length=20)
    email=models.EmailField(max_length=20)
    address=models.TextField()
    mobile=models.IntegerField(max_length=10)
    password=models.CharField(max_length=10)
    def __str__(self):
        return self.fname+" "+self.lname
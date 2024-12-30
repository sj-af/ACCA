from django.db import models

# Create your models here.
class Login(models.Model):
    username=models.CharField(max_length=100)
    password=models.CharField(max_length=10)
    def __str__(self) -> str:
        return self.username

class room(models.Model):
    
    user=models.IntegerField()
    text=models.TextField()
    def __str__(self) -> str:
        return self.text
    
    
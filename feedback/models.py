from django.db import models

# Create your models here.
class feedbackmodel(models.Model):
    name = models.CharField(max_length=50)
    age = models.PositiveIntegerField()
    email = models.EmailField()
    phone = models.PositiveBigIntegerField()
    desc = models.TextField(max_length=500)
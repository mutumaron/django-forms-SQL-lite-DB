from django.db import models

# Create your models here.

class Review(models.Model):
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100,null =True)
    user_email=models.EmailField(null =True)
    user_phone_number=models.CharField(max_length=10,null=True)
    review_text=models.TextField()
    rating=models.IntegerField()
    
    

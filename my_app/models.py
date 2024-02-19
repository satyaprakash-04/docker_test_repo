from django.db import models

# Create your models here.

class Customer(models.Model):
    customer_id = models.BigAutoField(primary_key=True)
    first_name = models.CharField(max_length=54, help_text='Customer First name')
    last_name = models.CharField(max_length=54, help_text='Customer Last name')
    user_email = models.EmailField(help_text='Customer Email')
    user_phone = models.EmailField(help_text='Customer Phone')
    password = models.CharField(max_length=544, help_text='Password')

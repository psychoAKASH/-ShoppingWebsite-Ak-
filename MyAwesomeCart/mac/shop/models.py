from django.db import models


# Create your models here.
class Product(models.Model):
    product_id = models.AutoField
    product_name = models.CharField(max_length=50)  # for product name
    desc = models.CharField(max_length=300)  # for product description
    pub_date = models.DateField()  # for product publish date

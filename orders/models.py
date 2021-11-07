
from django.db import models
class Order(models.Model):
    product_name = models.CharField(max_length=20,null=True)
    product_id=models.PositiveSmallIntegerField(null=True)
    product_quantity = models.IntegerField(null=True)
    Date_ordered=models.DateField(null=True)
    category_choices=(
        ('1','vegetable'),
        ('2','dry goods'),
        ('3','others'),
    )
    category=models.CharField(max_length=4, choices =category_choices, null=True)
    Supplier_id=models.CharField(primary_key=True,max_length=18)
    Supplier_email=models.EmailField(max_length=30,null=True)
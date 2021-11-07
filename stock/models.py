from django.db import models
from django.forms.fields import CharField


category_choice = (
	
		('Dry goods', 'Dry goods'),
		('Fruits & Vegetables', 'Fruits & Vegetables'),
      	('Meat', 'Meat'),
         	('Others', 'Others'),
	)

class Category(models.Model):
	name = models.CharField(max_length=50, blank=True, null=True)
	def __str__(self):
		return self.name
  


class Stock(models.Model):
   category = models.ForeignKey(Category, on_delete=models.CASCADE,blank=True)   
   item_name=models.CharField(max_length=50, blank=True,null=True)
   quantity=models.IntegerField(default='0', blank=True,null=True)
   received_quantity=models.IntegerField(default='0', blank=True,null=True)
   received_by=models.CharField(max_length=50, blank=True,null=True)
   issued_quantity=models.IntegerField(default='0', blank=True,null=True)
   issued_to=models.CharField(max_length=50, blank=True,null=True)
   reorder_level=models.IntegerField(default='0', blank=True,null=True)
   last_updated=models.DateTimeField(auto_now_add=False,auto_now=True)
   # export_to_csv=models.BooleanField(default=False)

# Create your models here.

   def __str__(self):
      return self.item_name+" "+str(self.quantity)
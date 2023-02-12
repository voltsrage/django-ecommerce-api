from django.db import models
# Used for many-to-many relationships
from mptt.models import MPTTModel, TreeForeignKey


# Create your models here.
class Category(MPTTModel):
	"""Create category model"""
	name = models.CharField(max_length=100, unique=True)
	# Many to many self join e.g. Clothes > Shoes Or Shirts and Apparel > Shoes or Shirts
	parent = TreeForeignKey("self", on_delete=models.PROTECT, null=True, blank=True)


	class MPTTMeta:
		order_insertion_by = ["name"]

	def __str__(self) -> str:
		return self.name

class Brand(models.Model):
	"""Create brand model"""
	name = models.CharField(max_length=100, unique=True)

	def __str__(self) -> str:
		return self.name


class Product(models.Model):
	"""Create product model"""
	name = models.CharField(max_length=100)
	description = models.TextField(blank=True)
	is_digital = models.BooleanField(default=False)
	brand = models.ForeignKey(Brand,on_delete=models.CASCADE)
	category = TreeForeignKey('Category', on_delete=models.SET_NULL, null=True, blank=True)

	def __str__(self) -> str:
		return self.name
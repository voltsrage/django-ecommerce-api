from rest_framework import serializers

from .models import Brand, Category, Product


class CategorySerializer(serializers.ModelSerializer):
	class Meta:
		model = Category
		fields = "__all__"
		read_only_fields = ['id']

class BrandSerializer(serializers.ModelSerializer):
	class Meta:
		model = Brand
		fields = "__all__"
		read_only_fields = ['id']

class ProductSerializer(serializers.ModelSerializer):
	brand = BrandSerializer()
	category = CategorySerializer()
	class Meta:
		model = Product
		fields = "__all__"
		read_only_fields = ['id']
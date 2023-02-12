from django.shortcuts import get_object_or_404, render
from drf_spectacular.utils import extend_schema
from rest_framework import viewsets
from rest_framework.response import Response

from .models import Brand, Category, Product
from .serializers import BrandSerializer, CategorySerializer, ProductSerializer

# Create your views here.



class CategoryViewSet(viewsets.ViewSet):
	"""A simple viewset viewing all categories"""

	queryset = Category.objects.all()

	@extend_schema(responses=CategorySerializer)
	def list(self ,request):
		serializer = CategorySerializer(self.queryset, many=True)
		return Response(serializer.data)

	def retrieve(self, request, pk=None):
		category = get_object_or_404(self.queryset, pk=pk)
		serializer = CategorySerializer(category)
		return Response(serializer.data)


class BrandViewSet(viewsets.ViewSet):
	"""A simple viewset viewing all Brands"""

	queryset = Brand.objects.all()

	@extend_schema(responses=BrandSerializer)
	def list(self,request):
		serializer = BrandSerializer(self.queryset, many=True)
		return Response(serializer.data)

	def retrieve(self, request, pk=None):
		brand = get_object_or_404(self.queryset, pk=pk)
		serializer = BrandSerializer(brand)
		return Response(serializer.data)


class ProductViewSet(viewsets.ViewSet):
	"""A simple viewset viewing all Brands"""

	queryset = Product.objects.all()

	@extend_schema(responses=ProductSerializer)
	def list(self,request):
		serializer = ProductSerializer(self.queryset, many=True)
		return Response(serializer.data)


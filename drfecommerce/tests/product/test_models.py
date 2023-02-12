import pytest

pytestmark = pytest.mark.django_db


class TestCategoryModel:
	def test_str_method(self, category_factory):
		x = category_factory(name="new_category")

		assert x.__str__() == 'new_category'


class TestProductModel:
	def test_str_method(self, product_factory):
		x = product_factory(name="new_product")

		assert x.__str__() == 'new_product'


class TestBrandModel:
	def test_str_method(self,  brand_factory):
		x = brand_factory(name="new_brand")

		assert x.__str__() == 'new_brand'
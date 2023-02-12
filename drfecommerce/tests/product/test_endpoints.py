
import json

import pytest

pytestmark = pytest.mark.django_db


class TestCategoryEndPoints:
	endpoint = "/api/category/"

	def test_category_get(self, category_factory, api_client):
		category_factory.create_batch(7)

		response = api_client().get(self.endpoint)

		assert response.status_code == 200
		assert len(json.loads(response.content)) == 7


class TestBrandEndPoints:
	endpoint = "/api/brand/"

	def test_category_get(self, brand_factory, api_client):
		brand_factory.create_batch(5)

		response = api_client().get(self.endpoint)

		assert response.status_code == 200
		assert len(json.loads(response.content)) == 5


class TestProductEndPoints:
	endpoint = "/api/product/"

	def test_category_get(self, product_factory, api_client):
		product_factory.create_batch(8)

		response = api_client().get(self.endpoint)

		assert response.status_code == 200
		assert len(json.loads(response.content)) == 8
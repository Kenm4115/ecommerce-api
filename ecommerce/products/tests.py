
from rest_framework.test import APITestCase
from rest_framework import status
from .models import Product
from django.urls import reverse

class ProductTests(APITestCase):

    def setUp(self):
        self.product_data = {
            'name': 'Test Product',
            'description': 'Test Description',
            'price': 100.00,
            'category': 'electronics',
            'stock_quantity': 10,
            'image_url': 'http://example.com/product.jpg'
        }

    def test_create_product(self):
        url = reverse('product-list-create')
        response = self.client.post(url, self.product_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_product_list(self):
        Product.objects.create(**self.product_data)
        url = reverse('product-list-create')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 1)

    def test_product_search(self):
        Product.objects.create(**self.product_data)
        url = reverse('product-list-create') + '?search=Test'
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreater(len(response.data['results']), 0)

    def test_filter_by_category(self):
        Product.objects.create(**self.product_data)
        url = reverse('product-list-create') + '?category=electronics'
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreater(len(response.data['results']), 0)


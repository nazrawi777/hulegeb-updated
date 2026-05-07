from django.test import TestCase
from django.urls import reverse

from .models import Category, Product, SubCategory


class ProductApiTests(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name="Sanitary", slug="sanitary")
        self.subcategory = SubCategory.objects.create(
            category=self.category,
            name="Brushes",
            slug="brushes",
        )
        self.product = Product.objects.create(
            category=self.category,
            subcategory=self.subcategory,
            name="Crimson Track Brush",
            price="450.00",
            description="Durable handmade brush.",
            short_description="Durable brush",
            image_url="https://example.com/brush.jpg",
        )

    def test_products_api_returns_active_products(self):
        response = self.client.get(reverse('api_products'), HTTP_HOST='hulegebbirhan.org')

        self.assertEqual(response.status_code, 200)
        payload = response.json()
        self.assertEqual(len(payload['products']), 1)
        self.assertEqual(payload['products'][0]['id'], self.product.id)
        self.assertEqual(payload['products'][0]['category'], 'sanitary')
        self.assertEqual(payload['products'][0]['subcategory'], 'brushes')

    def test_product_detail_api_returns_single_product(self):
        response = self.client.get(
            reverse('api_product_detail', kwargs={'product_id': self.product.id}),
            HTTP_HOST='hulegebbirhan.org',
        )

        self.assertEqual(response.status_code, 200)
        payload = response.json()
        self.assertEqual(payload['title'], 'Crimson Track Brush')
        self.assertEqual(payload['price'], 450.0)
        self.assertEqual(payload['image'], 'https://example.com/brush.jpg')

    def test_categories_api_nests_subcategories(self):
        response = self.client.get(reverse('api_categories'), HTTP_HOST='hulegebbirhan.org')

        self.assertEqual(response.status_code, 200)
        payload = response.json()
        self.assertEqual(payload['categories'][0]['slug'], 'sanitary')
        self.assertEqual(payload['categories'][0]['subcategories'][0]['slug'], 'brushes')

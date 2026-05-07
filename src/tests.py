from django.test import TestCase
from django.urls import reverse

from .models import (
    BankAccount,
    Category,
    DonationPurpose,
    Product,
    Programme,
    SubCategory,
    TeamMember,
)


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

class ContentCrudApiTests(TestCase):
    def test_team_api_returns_active_members(self):
        TeamMember.objects.create(
            name="Addisu Ketema Gema",
            role="General Manager",
            phone="+251 911721352",
            email="ketema.addisu@gmail.com",
            image_url="https://example.com/addisu.jpg",
        )
        TeamMember.objects.create(
            name="Hidden Member",
            role="Inactive",
            image_url="https://example.com/hidden.jpg",
            is_active=False,
        )

        response = self.client.get(reverse('api_team'), HTTP_HOST='hulegebbirhan.org')

        self.assertEqual(response.status_code, 200)
        payload = response.json()
        self.assertEqual(len(payload['team']), 1)
        self.assertEqual(payload['team'][0]['name'], "Addisu Ketema Gema")
        self.assertEqual(payload['team'][0]['image'], "https://example.com/addisu.jpg")

    def test_programmes_api_returns_active_programmes(self):
        Programme.objects.create(
            title="Women's empowerment",
            description="Providing resources, education, and advocacy.",
            image_url="https://example.com/programme.jpg",
        )
        Programme.objects.create(
            title="Hidden Programme",
            description="Inactive programme",
            image_url="https://example.com/hidden.jpg",
            is_active=False,
        )

        response = self.client.get(reverse('api_programmes'), HTTP_HOST='hulegebbirhan.org')

        self.assertEqual(response.status_code, 200)
        payload = response.json()
        self.assertEqual(len(payload['programmes']), 1)
        self.assertEqual(payload['programmes'][0]['title'], "Women's empowerment")
        self.assertEqual(payload['programmes'][0]['image'], "https://example.com/programme.jpg")

    def test_donation_info_api_returns_active_accounts_and_purposes(self):
        purpose = DonationPurpose.objects.create(label="General Donation")
        BankAccount.objects.create(
            purpose=purpose,
            bank_name="Commercial Bank of Ethiopia",
            account_number="1000 2000 3000",
            account_holder="Hulegeb",
        )
        BankAccount.objects.create(
            purpose=purpose,
            bank_name="Hidden Bank",
            account_number="999",
            is_active=False,
        )

        response = self.client.get(reverse('api_donation_info'), HTTP_HOST='hulegebbirhan.org')

        self.assertEqual(response.status_code, 200)
        payload = response.json()
        self.assertEqual(payload['purposes'][0]['label'], "General Donation")
        self.assertEqual(len(payload['bank_accounts']), 1)
        self.assertEqual(payload['bank_accounts'][0]['bank_name'], "Commercial Bank of Ethiopia")
        self.assertEqual(payload['bank_accounts'][0]['purpose'], "General Donation")


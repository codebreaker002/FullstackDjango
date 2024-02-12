from django.test import TestCase
from rest_framework.test import APIClient
from api.models import Item, Category, Tag

class ItemViewSetTestCase(TestCase):
    def setUp(self):
        # Create some sample categories
        electronics_category = Category.objects.create(name='Electronics')
        clothing_category = Category.objects.create(name='Clothing')
        books_category = Category.objects.create(name='Books')
        
        # Create some sample tags
        technology_tag = Tag.objects.create(name='Technology')
        fashion_tag = Tag.objects.create(name='Fashion')
        science_tag = Tag.objects.create(name='Science')
        
        # Create some test data and assign categories and tags
        Item.objects.create(sku='SKU1', name='Item 1', category=electronics_category, stock_status='In Stock', available_stock=10)
        Item.objects.create(sku='SKU2', name='Item 2', category=clothing_category, stock_status='Out of Stock', available_stock=0)

        # Add tags to items
        item1 = Item.objects.get(sku='SKU1')
        item1.tags.add(technology_tag, fashion_tag)

        item2 = Item.objects.get(sku='SKU2')
        item2.tags.add(science_tag)

    def test_filter_by_sku(self):
        client = APIClient()
        response = client.get('/items/?sku=SKU1/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['sku'], 'SKU1')

    def test_filter_by_name(self):
        client = APIClient()
        response = client.get('/items/?name=Item/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 2)

    def test_filter_by_category(self):
        client = APIClient()
        response = client.get('/items/?category=Electronics/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['category'], 'Electronics')

    def test_filter_by_tags(self):
        client = APIClient()
        response = client.get('/items/?tags=Technology,Fashion/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['sku'], 'SKU1')

    def test_filter_by_stock_status(self):
        client = APIClient()
        response = client.get('/items/?stock_status=In Stock/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['sku'], 'SKU1')
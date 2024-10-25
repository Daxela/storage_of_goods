from django.test import TestCase

# Create your tests here.

from .models import Product, Price, Type


class PriceListCreateViewTest(TestCase):

    @classmethod
    def setUp(cls):
        pass

    def test_view_url_get(self):
        resp = self.client.get('/api/prices/')
        self.assertEqual(resp.status_code, 200)

    def test_view_url_post(self):
        resp = self.client.post('/api/prices/', body={"currency": "RUB", "cost": 15})
        self.assertEqual(resp.status_code, 201)


class TypeListCreateViewTest(TestCase):

    @classmethod
    def setUp(cls):
        pass

    def test_view_url_get(self):
        resp = self.client.get('/api/types/')
        self.assertEqual(resp.status_code, 200)

    def test_view_url_post(self):
        resp = self.client.post('/api/types/', body={"name": "Напитки", "description": "Описание типа напитки"})
        self.assertEqual(resp.status_code, 201)


class ProductListCreateViewTest(TestCase):

    @classmethod
    def setUp(cls):
        Price.objects.create(currency="RUB", cost=15)
        Type.objects.create(name="Напитки", description="Описание типа напитки")

    def test_view_url_get(self):
        resp = self.client.get('/api/products/')
        self.assertEqual(resp.status_code, 200)

    def test_view_url_post(self):
        resp = self.client.post('/api/products/',
                                body={"name": "Вода", "price": 1, "quantity": 20, "barcode": "123456789", "type": 1})
        self.assertEqual(resp.status_code, 201)


class PriceRetrieveUpdateDeleteViewTest(TestCase):

    def setUp(self):
        self.price = Price.objects.create(currency="RUB", cost=15)

    def test_view_url_get(self):
        resp = self.client.get(f'/api/prices/{self.price.id}/')
        self.assertEqual(resp.status_code, 200)

    def test_view_url_put(self):
        resp = self.client.put(f'/api/prices/{self.price.id}/',
                               body={"id": self.price.id, "currency": "USD", "cost": 17})
        self.assertEqual(resp.status_code, 200)

    def test_view_url_patch(self):
        resp = self.client.patch(f'/api/prices/{self.price.id}/', body={"cost": 19})
        self.assertEqual(resp.status_code, 200)

    def test_view_url_delete(self):
        resp = self.client.delete(f'/api/prices/{self.price.id}/')
        self.assertEqual(resp.status_code, 204)


class TypeRetrieveUpdateDeleteViewTest(TestCase):

    def setUp(self):
        self.type = Type.objects.create(name="Напитки", description="Описание типа напитки")

    def test_view_url_get(self):
        resp = self.client.get(f'/api/types/{self.type.id}/')
        self.assertEqual(resp.status_code, 200)

    def test_view_url_put(self):
        resp = self.client.put(f'/api/types/{self.type.id}/',
                               body={"id": self.type.id, "name": "Выпечка", "description": "Описание типа выпечка"})
        self.assertEqual(resp.status_code, 200)

    def test_view_url_patch(self):
        resp = self.client.patch(f'/api/types/{self.type.id}/', body={"description": "Подробное описание типа выпечка"})
        self.assertEqual(resp.status_code, 200)

    def test_view_url_delete(self):
        resp = self.client.delete(f'/api/types/{self.type.id}/')
        self.assertEqual(resp.status_code, 204)


class ProductRetrieveUpdateDeleteViewTest(TestCase):

    def setUp(self):
        self.price = Price.objects.create(currency="RUB", cost=15)
        self.type = Type.objects.create(name="Напитки", description="Описание типа напитки")
        self.product = Product.objects.create(name="Вода", price=self.price, quantity=20, barcode="123456789",
                                              type=self.type)

    def test_view_url_get(self):
        resp = self.client.get(f'/api/products/{self.product.id}/')
        self.assertEqual(resp.status_code, 200)

    def test_view_url_put(self):
        resp = self.client.put(f'/api/products/{self.product.id}/',
                               body={"id": self.product.id, "name": "Сок", "price": self.price, "quantity": 5,
                                     "barcode": "987654321", "type": self.type})
        self.assertEqual(resp.status_code, 200)

    def test_view_url_patch(self):
        resp = self.client.patch(f'/api/products/{self.product.id}/', body={"quantity": 100})
        self.assertEqual(resp.status_code, 200)

    def test_view_url_delete(self):
        resp = self.client.delete(f'/api/products/{self.product.id}/')
        self.assertEqual(resp.status_code, 204)


class ProductViewTest(TestCase):

    def setUp(self):
        self.price = Price.objects.create(currency="RUB", cost=15)
        self.type = Type.objects.create(name="Напитки", description="Описание типа напитки")
        self.product = Product.objects.create(name="Морс", price=self.price, quantity=500, barcode="123456789",
                                              type=self.type)

    def test_view_url_none(self):
        resp = self.client.post('/api/products/quantity/', data={})
        self.assertEqual(resp.status_code, 400)

    def test_view_url_true(self):
        resp = self.client.post('/api/products/quantity/', data={"product_id": self.product.id, "quantity_sold": 1})
        self.assertEqual(resp.status_code, 200)

    def test_view_url_false(self):
        resp = self.client.post('/api/products/quantity/', data={"product_id": self.product.id + 1, "quantity_sold": 1})
        self.assertEqual(resp.status_code, 404)

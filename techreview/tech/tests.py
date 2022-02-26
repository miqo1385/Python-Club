from django.test import TestCase
from django.contrib.auth.models import User
from .models import ProductType, Product, Review 

# Create your tests here.

class ProductTypeTest(TestCase):
    def setUp(self):
        self.type=ProductType(typename='Lenovo Laptop')

    def test_typestring(self):
        self.assertEqual(str(self.type), 'Lenovo Laptop')

    def test_tablename(self):
        self.assertEqual(str(ProductType._meta.db_table), 'producttype')



class ProductTest(TestCase):
    def setUp(self):
        self.type=ProductType(typename='Laptop')
        self.user=User(username='user1')
        self.product=Product(productname='Lenovo', producttype=self.type, user=self.user, productentrydate=(2021,1,10), productprice=1200.99, producturl='http://www.lenovo.com', productdescription='lenovo laptop')

    def test_string(self):
        self.assertEqual(str(self.product),'Lenovo')

    def test_discount(self):
        disc= self.product.productprice * .05
        self.assertEqual(self.product.discountAmount(), disc)

        

    
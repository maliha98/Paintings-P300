from django.db import models


class Category(models.Model):
    category = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.category
# Create your models here.


class Product(models.Model):
    title = models.CharField(max_length=100, null=True)
    description = models.CharField(max_length=1000, null=True)
    product_image = models.ImageField(default="product.jpg", null=True)
    category = models.ForeignKey(Category, null=True, on_delete=models.CASCADE)
    price = models.FloatField('Price : $', null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.title

from django.db import models
from product.models import Product
from django.contrib.auth.models import User


class Cart(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, null=True, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    purchased = models.BooleanField(default=False)

    def __str__(self):
        return self.product.title

    def productTotal(self):
        t = self.product.price * self.quantity
        return t

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


class Order_Product(models.Model):
    CHOICES = (
        ('Pending', 'Pending'),
        ('Delivered', 'Delivered'),
        ('Cancled', 'Cancled'),
    )
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    cartitem = models.ManyToManyField(Cart)
    ordered = models.BooleanField(default=False)
    status = models.CharField(
        max_length=100, null=True, choices=CHOICES, default=CHOICES[0][0])

    def __str__(self):
        return self.user.first_name

    def orderTotal(self):
        t = 0
        for i in self.cartitem.all():
            t += i.productTotal()
        return t

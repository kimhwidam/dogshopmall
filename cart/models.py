from django.db import models
from user.models import User
from product.models import Product

class Cart(models.Model):
    cart_id = models.AutoField(primary_key=True)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    count = models.IntegerField()

    class Meta:
        db_table = 'my_cart'
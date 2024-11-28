from django.db import models
from user.models import User
from product.models import Product


# Create your models here.
pay_type = (
    ('a', '계좌이체'),
    ('b', '무통장 입금'),
    ('c', '카드'),
)
class Order(models.Model):

    order_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    create_dt = models.DateTimeField(auto_now_add=True)
    update_dt = models.DateTimeField(auto_now_add=True)
    address = models.CharField(max_length=100, null=True, blank=True, default="")
    request = models.TextField(blank=True) 
    pay = models.CharField(max_length=10, choices=pay_type)

    class Meta:
        db_table = 'my_order'

class Order_Detail(models.Model):
    pay_type = (
        ('a', '계좌이체'),
        ('b', '무통장 입금'),
        ('c', '카드'),
    )
    
    order_detial_id = models.AutoField(primary_key=True)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    # order_id = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True) # 상품 참조 추가
    price = models.IntegerField()
    count = models.IntegerField()
    pay = models.CharField(max_length=10, choices=pay_type)
    # address = models.CharField(max_length=100)

    class Meta:
        db_table = 'my_order_detail'

from django.db import models
from user.models import User
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class Product(models.Model):
    product_id = models.CharField(primary_key=True, max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    brand = models.CharField(max_length=255)
    price = models.IntegerField()
    image = models.ImageField()
    cp = models.IntegerField()
    cf = models.IntegerField()
    cr = models.IntegerField()
    cb = models.IntegerField()
    ca = models.IntegerField()
    po = models.IntegerField()
    wa = models.IntegerField()
    
    def __str__(self):
        return f"{self.name} ({self.product_id})"

    class Meta:
        db_table = 'my_product'

class Review(models.Model):
    review_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    rating = models.IntegerField(validators=[MinValueValidator(1),
                                       MaxValueValidator(5)])
    content = models.TextField()
    create_dt = models.DateTimeField()
    updata_dt = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        db_table = 'my_review'
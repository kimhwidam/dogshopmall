from django.db import models
from product.models import Product, User
import random

class DogSurvey(models.Model):
    Unnamed = models.IntegerField(primary_key=True)
    이름 = models.CharField(max_length=255)
    이메일 = models.EmailField()
    견종 = models.CharField(max_length=255)
    견종_코드 = models.CharField(max_length=255)
    크기 = models.CharField(max_length=255)
    크기_코드 = models.CharField(max_length=255)
    색상 = models.CharField(max_length=255)
    색상_코드 = models.CharField(max_length=255)
    연령대 = models.CharField(max_length=255)
    연령대_코드 = models.CharField(max_length=255)
    상태 = models.CharField(max_length=255)
    상태_코드 = models.CharField(max_length=255)
    브랜드 = models.CharField(max_length=255)
    브랜드_코드 = models.CharField(max_length=255)
    사료 = models.CharField(max_length=255)
    사료_코드 = models.CharField(max_length=255)
    평점 = models.IntegerField()
    후기 = models.TextField(max_length=255)
    주소 = models.CharField(max_length=255)
    국가 = models.CharField(max_length=255)
    시도 = models.CharField(max_length=255)
    시군구 = models.CharField(max_length=255)
    CP = models.IntegerField()
    CF = models.IntegerField()
    CR = models.IntegerField()
    CB = models.IntegerField()
    CA = models.IntegerField()
    PO = models.IntegerField()
    WA = models.IntegerField()
    field_8 = models.CharField(max_length=255)
    field_9 = models.CharField(max_length=255)
    field_10 = models.CharField(max_length=255)
    field_11 = models.CharField(max_length=255)
    field_12 = models.CharField(max_length=255)
    field_13 = models.CharField(max_length=255)
    field_14 = models.CharField(max_length=255)
    field_15 = models.CharField(max_length=255)
    field_16 = models.CharField(max_length=255)
    field_17 = models.CharField(max_length=255)
    field_18 = models.CharField(max_length=255)
    field_19 = models.CharField(max_length=255)
    field_20 = models.CharField(max_length=255)
    field_21 = models.CharField(max_length=255)
    field_22 = models.CharField(max_length=255)
    field_23 = models.CharField(max_length=255)
    field_24 = models.CharField(max_length=255)
    field_25 = models.CharField(max_length=255)
    field_26 = models.CharField(max_length=255)
    field_27 = models.CharField(max_length=255)
    field_28 = models.CharField(max_length=255)
    field_29 = models.CharField(max_length=255)
    field_30 = models.CharField(max_length=255)
    field_31 = models.CharField(max_length=255)
    field_32 = models.CharField(max_length=255)
    field_33 = models.CharField(max_length=255)
    field_34 = models.CharField(max_length=255)
    field_35 = models.CharField(max_length=255)
    field_36 = models.CharField(max_length=255)
    field_37 = models.CharField(max_length=255)
    field_38 = models.CharField(max_length=255)
    field_39 = models.CharField(max_length=255)
    field_40 = models.CharField(max_length=255)
    field_41 = models.CharField(max_length=255)
    field_42 = models.CharField(max_length=255)
    field_43 = models.CharField(max_length=255)
    field_44 = models.CharField(max_length=255)
    field_45 = models.CharField(max_length=255)
    field_46 = models.CharField(max_length=255)
    field_47 = models.CharField(max_length=255)
    field_48 = models.CharField(max_length=255)
    field_49 = models.CharField(max_length=255)
    field_50 = models.CharField(max_length=255)
    field_51 = models.CharField(max_length=255)
    field_52 = models.CharField(max_length=255)
    field_53 = models.CharField(max_length=255)
    field_54 = models.CharField(max_length=255)
    field_55 = models.CharField(max_length=255)
    field_56 = models.CharField(max_length=255)
    field_57 = models.CharField(max_length=255)
    field_58 = models.CharField(max_length=255)
    field_59 = models.CharField(max_length=255)
    field_60 = models.CharField(max_length=255)
    field_61 = models.CharField(max_length=255)
    field_62 = models.CharField(max_length=255)
    field_63 = models.CharField(max_length=255)
    field_64 = models.CharField(max_length=255)
    field_65 = models.CharField(max_length=255)
    field_66 = models.CharField(max_length=255)
    field_67 = models.CharField(max_length=255)
    field_68 = models.CharField(max_length=255)
    field_69 = models.CharField(max_length=255)
    field_70 = models.CharField(max_length=255)
    field_71 = models.CharField(max_length=255)
    field_72 = models.CharField(max_length=255)
    field_73 = models.CharField(max_length=255)
    field_74 = models.CharField(max_length=255)
    field_75 = models.CharField(max_length=255)
    field_76 = models.CharField(max_length=255)
    field_77 = models.CharField(max_length=255)
    field_78 = models.CharField(max_length=255)
    field_79 = models.CharField(max_length=255)
    field_80 = models.CharField(max_length=255)
    field_81 = models.CharField(max_length=255)
    field_82 = models.CharField(max_length=255)
    field_83 = models.CharField(max_length=255)

    # product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def as_product(self):  # avoid circular import
        product = Product()
        user = User.objects.first()  # 첫 번째 User 객체를 가져옵니다.

        product.product_id = self.사료_코드
        product.name = self.사료
        product.brand = self.브랜드
        product.price = random.randint(10000, 100000)  # 랜덤 가격 설정
        product.cp = self.CP
        product.cf = self.CF
        product.cr = self.CR
        product.cb = self.CB
        product.ca = self.CA
        product.po = self.PO
        product.wa = self.WA
        product.image = 'media/' + self.사료_코드 + '.jpg'  

        if user is not None:  
            product.user_id = user.id  
        else:
            raise ValueError("No users found")  

        product.save() 
        return product

    class Meta:
        # managed = False
        db_table = 'dog_info'

from django import forms
from .models import Order, Order_Detail
from cart.models import Cart

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['address', 'request']
        labels = {
            'address': '주소',
            'request': '요청사항',
        }

class OrderDetailForm(forms.ModelForm):
    class Meta:
        model = Order_Detail
        fields = ['product', 'price', 'count', 'pay']
        labels = {
            'product': '상품',
            'price': '가격',
            'count': '수량',
            'pay': '결제수단',
        }



# forms.py
class OrderCreateForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['address', 'request','pay']
        labels = {
            'address': '주소',
            'request': '요청사항',
        }

    def __init__(self, *args, **kwargs):
        super(OrderCreateForm, self).__init__(*args, **kwargs)
        self.fields['pay'] = forms.ChoiceField(choices=Order_Detail.pay_type, label='결제수단')

    def save(self, commit=True):
        order = super().save(commit=False)
        if commit:
            order.save()
            for item in Cart.objects.filter(user=order.user):
                pay_value = next((display for value, display in Order_Detail.pay_type if value == self.cleaned_data['pay']), None)
                Order_Detail.objects.create(
                    order=order, 
                    product=item.product_id, 
                    count=item.count, 
                    price=item.product_id.price,
                    pay= order.pay,
                )
        return order

# order/views.py
from django.shortcuts import render, redirect
from .models import Order, Order_Detail
from product.models import Product
from django.contrib.auth.decorators import login_required
from cart.models import Cart
from .forms import OrderForm, OrderDetailForm
from .forms import OrderCreateForm


# views.py
def order_list(request):
    user_orders = Order.objects.filter(user=request.user)
    user_order_details = Order_Detail.objects.filter(order__in=user_orders)

    return render(request, 'order/order_list.html', {'user_orders': user_orders, 'user_order_details': user_order_details})


def order_list2(request):
    user_orders2 = Product.objects.values('product_id','name','brand','image')
    
    return render(request, 'order/order_list.html', {'user_orders2': user_orders2})

@login_required
def order_create(request):
    cart_items = Cart.objects.filter(user=request.user)
    total_price = sum(item.product_id.price * item.count for item in cart_items)

    if request.method == 'POST':
        order_form = OrderCreateForm(request.POST)
        if order_form.is_valid():
            order = order_form.save(commit=False)
            order.user = request.user
            order.save()

            for item in cart_items:
                Order_Detail.objects.create(order=order, product=item.product_id, count=item.count, price=item.product_id.price)

            cart_items.delete()

            return redirect('order_list')
    else:
        order_form = OrderCreateForm()

    context = {'order_form': order_form, 'cart_items': cart_items, 'total_price': total_price}
    return render(request, 'order/order_create.html', context)



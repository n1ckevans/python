from django.shortcuts import render, redirect
from .models import Order, Product
from django.db.models import Avg, Count, Min, Sum

def index(request):
    context = {
        "all_products": Product.objects.all()
    }
    return render(request, "store/index.html", context)


def checkout_buffer(request):
    last_order = Order.objects.last()
    last_order_quantity = last_order.quantity_ordered
    last_price = last_order.total_price
    total_price = Order.objects.aggregate(Sum('total_price')).get('total_price__sum', 0.0)

    context = {
        "total": last_price,
        "quantity": Order.objects.count(),
        "total_price": total_price,
    }

    return render(request, "store/checkout.html", context)

def checkout(request):
    quantity_from_form = int(request.POST["quantity"])
    price_from_form = float(request.POST["price"])
    total_charge = quantity_from_form * price_from_form
    print("Charging credit card...")
    Order.objects.create(quantity_ordered=quantity_from_form, total_price=total_charge)

  


    return redirect("/checkout_buffer")
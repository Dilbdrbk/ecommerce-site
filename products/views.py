from django.shortcuts import render,redirect
from products.models import Products, Carts
from django.contrib.auth.decorators import login_required




# Create your views here.
def product_detail(request, product_id):
    product = Products.objects.get(pk=product_id)
    product_data = {"product": product}
    return render(request, "product_detail.html", product_data)

@login_required
def shopping_carts(request):
    carts_data = Carts.objects.filter(user_id=request.user.pk)
    has_cart = len(carts_data)>0
    if has_cart:
        cart_total= sum([cart.cart_total for cart in carts_data])
    context = {"carts": carts_data, "has_cart":has_cart, "cart_total":cart_total}
    return render(request, "shopping_carts.html", context)


@login_required
def add_to_cart(request, product_id):
    product = Products.objects.get(pk=product_id)
    cart_data = {
        "user_id": request.user.pk,
        "product_id": product_id,
        "cart_quantity": 1,
        "cart_total": product.price,
    }
    has_quantity_from_post = False
    if request.method == "POST":
        quantity = request.POST.get("quantity", 1)
        has_quantity_from_post = True
        cart_data["cart_quantity"] = quantity

    if Carts.objects.filter(user_id=request.user.pk, product_id=product_id).exists():
        cart_item = Carts.objects.get(user_id=request.user.pk, product_id=product_id)
        if has_quantity_from_post:
            cart_item.cart_quantity = cart_data["cart_quantity"]
            cart_item.cart_total = int(cart_data["cart_quantity"]) * product.price
            cart_item.save()
        else:
            cart_item.cart_quantity += 1
            cart_item.cart_total = int(cart_item.cart_quantity) * product.price
            cart_item.save()
    else:
        Carts.objects.create(**cart_data)
    return redirect("shopping_carts")

@login_required
def remove_cart_item(request, cart_id):
    Carts.objects.filter(pk=cart_id).delete()
    return redirect ("shopping_carts")
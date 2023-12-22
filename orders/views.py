from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from products.models import Carts
import uuid
from orders.models import Orders

# Create your views here.
@login_required
def checkout(request):
      
      cart_items = Carts.objects.filter(user=request.user.id)
      cart_total = sum([cart.cart_total for cart in cart_items])
      SHIPPING_FEE = 100
      TAX = 0.13
      DISCOUNT = 0.05
      order_total = cart_total+ SHIPPING_FEE +(cart_total*TAX) - (cart_total*DISCOUNT)

      order_data={
           
            "cart_items":cart_items,
            "cart_total":cart_total,
            "shipping_fee":SHIPPING_FEE,
            "tax":TAX * cart_total,
            "discount":cart_total*DISCOUNT,
            "order_total":order_total,
      }
      product_data = []
      for item in cart_items:
            product_data.append({
                  "title":item.product.title,
                  "price":item.product.price,
                  "image":item.product.image,
                  "quantity":item.product.quantity,
                  "cart_total":item.cart_total

            })
      if request.method == "POST":
            address = request.POST.get("address")
            city = request.POST.get("city")
            house_number =  request.POST.get("house_number")
            mobile_number = request.POST.get("mobile_number")
            message = request.POST.get("message")
            order_data_for_db={
                "tracking_id": str(uuid.uuid4()),
                "user_id":request.user.id,
                "address":address,
                "city":city,
                "house_number": house_number,
                "mobile_number":mobile_number,
                "message":message,
                "order_total": order_total,
                "products" : product_data,
                "status": "pending"
            }
            print(order_data_for_db)
            Orders.objects.create(**order_data_for_db)
            return redirect("purchase_complete")
    

      return render(request, "checkout.html", order_data)

@login_required
def purchase_complete(request):
      return render(request,"purchase_done.html")

@login_required
def order_summary(request):
      #top five orders
      orders = Orders.objects.filter(user=request.user).order_by("-updated_at")[0:5]
      order_data={
          "orders": orders
      }
      return render(request, "order_summary.html",order_data)
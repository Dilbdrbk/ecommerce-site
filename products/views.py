from django.shortcuts import render

# Create your views here.
def product_detail(request):
    return render(request, "product_detail.html")

def shopping_carts(request):
    return render(request, "shopping_carts.html")

from django.urls import path
import products.views as product_views

urlpatterns = [
    path("detail",product_views.product_detail, name="product_details"),
    path("carts",product_views.shopping_carts, name="shopping_carts"),
]

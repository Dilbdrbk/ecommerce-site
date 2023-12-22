from django.urls import path
import orders.views as order_views

urlpatterns = [
    path("checkout",order_views.checkout, name="checkout"),
    path("purchase_complete",order_views.purchase_complete, name="purchase_complete"),
    path("summary",order_views.order_summary, name="order_summary")
]
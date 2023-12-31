from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",include("users.urls")),
    path("product/",include("products.urls")),
    path("order/",include("orders.urls"))
    ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

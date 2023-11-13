from django.contrib import admin
from django.urls import path, include
from product import views
from .swagger import urlpatterns as swagger_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('product.urls')),
    path('api/v1/', include('users.urls'))
]

urlpatterns += swagger_urlpatterns

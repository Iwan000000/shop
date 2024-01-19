from django.urls import path
from shoping.views import index, product, product_information
from . import views

app_name = 'shoping'  # Указываем пространство имен для приложения "shoping"

urlpatterns = [
    path('', index, name="index"),
    path('<int:pk>/product/', product, name="product"),
    path('<int:pk>/product_information/', product_information, name="product_information"),


]

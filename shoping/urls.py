from itertools import product

from django.urls import path

from shoping.views import index

urlpatterns = [
    path('', index, name="index"),

]

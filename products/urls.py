from django.urls import path
from .views import (
    home,
    add_product,
    edit_product,
    delete_product,
    product_detail
)

urlpatterns = [
    path('', home, name='home'),
    path('add/', add_product, name='add_product'),
    path('edit/<int:product_id>/', edit_product, name='edit_product'),
    path('delete/<int:product_id>/', delete_product, name='delete_product'),
    path('product/<int:product_id>/', product_detail, name='product_detail'),
]

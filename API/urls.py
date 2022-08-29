from django.urls import path
from .views import ListCategory, DetailsCategory, ListProduct, DetailsProduct

urlpatterns = [
    path('categories', ListCategory.as_view(), name='categories'),
    path('categories/<int:pk>/', DetailsCategory.as_view(), name='singlecategory'),
    path('products', ListProduct.as_view(), name='products'),
    path('products/<int:pk>/', DetailsProduct.as_view(), name='singleproduct'),
    
]
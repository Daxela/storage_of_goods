from django.urls import path
from . import views

urlpatterns = [
    path('products/', views.ProductListCreate.as_view()),
    path('products/<int:pk>/', views.ProductRetrieveUpdateDelete.as_view()),
    path('products/quantity/', views.ProductView.as_view()),
    path('prices/', views.PriceListCreate.as_view()),
    path('prices/<int:pk>/', views.PriceRetrieveUpdateDelete.as_view()),
    path('types/', views.TypeListCreate.as_view()),
    path('types/<int:pk>/', views.TypeRetrieveUpdateDelete.as_view()),
]
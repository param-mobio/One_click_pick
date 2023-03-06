from django.urls import path,include
from products.views import index,createproduct,products,updateproduct,deleteproduct
urlpatterns = [
    path('index/',index.Index.as_view(),name ='index'),
    path('createproduct/', createproduct.CreateProduct.as_view(), name='createproduct'),
    path('products/',products.UserProducts.as_view(),name='products'),
    path('updateproduct/<str:pk>',updateproduct.UpdateProduct.as_view(),name='updateproduct'),
    path('deleteproduct/<str:pk>',deleteproduct.DeleteProduct.as_view(),name='deleteproduct'),
]

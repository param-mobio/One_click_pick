from django.urls import path,include
from products.views import index,createproduct,products,updateproduct,deleteproduct,shop,new,details
urlpatterns = [
    path('index/',index.Index.as_view(),name ='index'),
    path('createproduct/', createproduct.CreateProduct.as_view(), name='createproduct'),
    path('products/',products.UserProducts.as_view(),name='products'),
    path('updateproduct/<str:pk>',updateproduct.UpdateProduct.as_view(),name='updateproduct'),
    path('deleteproduct/<str:pk>',deleteproduct.DeleteProduct.as_view(),name='deleteproduct'),
    path('shop/',shop.Shop.as_view(),name ='shop'),
    path('new/',new.New.as_view(),name='new'),
    path('detail/<str:pk>',details.Details.as_view(),name='detail'),
]

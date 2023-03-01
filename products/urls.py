from django.urls import path,include
from products.views import index,createproduct
urlpatterns = [
    path('index/',index.Index.as_view(),name ='index'),
    path('createproduct/', createproduct.CreateProduct.as_view(), name='createproduct'),
]

from django.urls import path  
from .views import SellersCreateAPIView, SellersDetailAPIView, ChargeAPIView

urlpatterns = [  
    path('', SellersCreateAPIView.as_view(), name='client-create'), 
    path('<uuid:id>/', SellersDetailAPIView.as_view(), name='client-update'),
    path('charge/', ChargeAPIView.as_view(), name='charge'),

]  
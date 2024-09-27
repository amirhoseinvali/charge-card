from django.urls import path  
from .views import ClientCreateAPIView, ClientDetailAPIView

urlpatterns = [  
    path('', ClientCreateAPIView.as_view(), name='client-create'), 
    path('<uuid:id>/', ClientDetailAPIView.as_view(), name='client-update'),
]  
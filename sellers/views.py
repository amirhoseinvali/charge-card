from rest_framework import viewsets, permissions
from .models import Sellers, Charge
from .serializers import SellersSerializer, ChargeSerializer
from rest_framework import generics 
from django.contrib.auth.models import User


# Create your views here.
class SellersCreateAPIView(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Sellers.objects.all()
    serializer_class = SellersSerializer


class SellersDetailAPIView(generics.RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Sellers.objects.all()
    serializer_class = SellersSerializer
    lookup_field = 'id'


class SellersDetailAPIView(generics.RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Sellers.objects.all()
    serializer_class = SellersSerializer
    lookup_field = 'id'



class ChargeAPIView(generics.CreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Charge.objects.all()
    serializer_class = SellersSerializer





class ChargeAPIView(generics.CreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Charge.objects.all()
    serializer_class = ChargeSerializer

    def perform_create(self, serializer):
        seller = Sellers.objects.filter(user = self.request.user).first()
        if not seller:
             raise ValueError("You Are Not Seller!")
        if seller.has_open_charge_request():
            raise ValueError("You Have Open Charge Request!")

        serializer.save(seller=seller)


    # def update(self, request, *args, **kwargs):  
    #     instance = self.get_object()  

    #     # Ensure the seller is the current logged-in user  
    #     if instance.seller != request.user:  
    #         return Response({'error': 'You do not have permission to modify this charge.'}, status=status.HTTP_403_FORBIDDEN)  

    #     amount_to_add = request.data.get('amount', None)  

    #     if amount_to_add is None:  
    #         return Response({'error': 'Amount to add is required'}, status=status.HTTP_400_BAD_REQUEST)  

    #     try:  
    #         amount_to_add = int(amount_to_add)  
    #         instance.increase_amount(amount_to_add)  # Call the model method to increase amount  
    #     except ValueError as e:  
    #         return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)  

    #     serializer = self.get_serializer(instance)  
    #     return Response(serializer.data, status=status.HTTP_200_OK) 
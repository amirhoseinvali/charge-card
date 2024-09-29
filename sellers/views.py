from rest_framework.permissions import IsAuthenticated
from .models import Sellers, Charge
from .serializers import SellersSerializer, ChargeSerializer, ConfirmChargeSerializer
from rest_framework import generics 
from django.contrib.auth.models import User
from django.db import transaction
import datetime
from rest_framework.response import Response  
from rest_framework import status
from utils import permissions, exceptions


class SellersCreateAPIView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated, permissions.IsAdmin]
    queryset = Sellers.objects.all()
    serializer_class = SellersSerializer



class SellersDetailAPIView(generics.RetrieveAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Sellers.objects.all()
    serializer_class = SellersSerializer
    lookup_field = 'id'



class ChargeAPIView(generics.CreateAPIView):
    permission_classes = [IsAuthenticated, permissions.IsSeller]
    queryset = Charge.objects.all()
    serializer_class = ChargeSerializer

    def perform_create(self, serializer):
        seller = Sellers.objects.filter(user=self.request.user).first()
        if seller.has_open_charge_request():
            raise exceptions.HasOpenChargeRequest()
        serializer.save(seller=seller)




class ConfirmChargeAPIView(generics.RetrieveUpdateAPIView):
    permission_classes = [IsAuthenticated, permissions.IsAdmin]
    queryset = Charge.objects.all()
    serializer_class = ConfirmChargeSerializer
    lookup_field = 'id'

    def post(self, request, *args, **kwargs):  
        charge = self.get_object()
        seller = Sellers.objects.get(id = charge.seller.id)
        with transaction.atomic():
            confirm_result = charge.confirm_charge(request.user)
            if confirm_result:
                seller.increase_inventory(charge.amount)
            return Response({"id":charge.id, "is_confirmed":charge.is_confirmed, "confirmed_time":charge.confirmed_time, "amount":charge.amount}, status=status.HTTP_201_CREATED)

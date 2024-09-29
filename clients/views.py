from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from sellers.models import Sellers
from .models import Client, ChargeRequests
from .serializers import ClientSerializer, ChargeRequestSerializer, ClientChargeSerializer
from rest_framework import generics 
from rest_framework.response import Response  
from rest_framework import status
from django.db import transaction
from utils import permissions, exceptions

class ClientCreateAPIView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated, permissions.IsAdmin]
    queryset = Client.objects.all()
    serializer_class = ClientSerializer


class ClientDetailAPIView(generics.RetrieveAPIView):
    permission_classes = [IsAuthenticated, permissions.IsAdmin]
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    lookup_field = 'id'


class ClientChargeslAPIView(generics.RetrieveAPIView):
    permission_classes = [IsAuthenticated, permissions.IsAdmin]
    queryset = ChargeRequests.objects.all()
    serializer_class = ClientChargeSerializer
    lookup_field = 'id'



class ChargeRequestCreateAPIView(generics.CreateAPIView):
    permission_classes = [IsAuthenticated, permissions.IsSeller]
    serializer_class = ChargeRequestSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            seller = Sellers.objects.filter(user=self.request.user).first()
            client = Client.objects.filter(phone_number=serializer.validated_data.pop('phone_number')).first()
            if not client:
                raise exceptions.ClientNotFound()
            with transaction.atomic():
                ChargeRequests.objects.create(client=client,seller = seller, **serializer.validated_data)
                seller.decrease_inventory(serializer.validated_data.get('amount'))
                client.increase_inventory(serializer.validated_data.get('amount'))
                serializer.validated_data['inventory'] = seller.get_inventory()
                return Response(serializer.validated_data, status=status.HTTP_201_CREATED)
            raise exceptions.ChargeClientFailed()

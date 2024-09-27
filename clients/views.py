from rest_framework import viewsets, permissions
from .models import Client
from .serializers import ClientSerializer  
from rest_framework import generics 

class ClientCreateAPIView(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Client.objects.all()
    serializer_class = ClientSerializer


class ClientDetailAPIView(generics.RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    lookup_field = 'id'
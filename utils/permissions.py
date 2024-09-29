from rest_framework.permissions import BasePermission  
from sellers.models import Sellers
from utils import exceptions


class IsAdmin(BasePermission):  
    def has_permission(self, request, view):  
        if request.user.is_authenticated and request.user.is_superuser:
            return True
        raise exceptions.NotAdmin()



class IsSeller(BasePermission):  
    def has_permission(self, request, view):
        if Sellers.objects.filter(user=request.user).first():
            return True
        raise exceptions.NotSeller()
    


class IsSellerActive(BasePermission):  
    def has_permission(self, request, view):
        seller = Sellers.objects.filter(user=request.user).first()
        if seller:
            if seller.is_active:
                return True
            raise exceptions.UserNotActive()

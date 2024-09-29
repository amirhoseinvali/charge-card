import uuid
from django.db import models
from django.utils.timezone import now
from sellers.models import Sellers
from utils.validators import phone_number_validator



class Client(models.Model):
    id = models.UUIDField(auto_created=True, primary_key=True, default=uuid.uuid4, editable=False)
    phone_number = models.CharField(unique=True, max_length=13, validators=[phone_number_validator])
    registration_date =  models.DateTimeField(default=now, blank=True, editable=False)
    inventory = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    def increase_inventory(self, amount_to_add):  
        if amount_to_add <= 0:  
            raise ValueError("Amount must be a positive integer.")  
        self.inventory += amount_to_add  
        self.save()

    def get_inventory(self):
        return self.inventory

class ChargeRequests(models.Model):
    id = models.UUIDField(auto_created=True, primary_key=True, default=uuid.uuid4, editable=False)
    seller = models.ForeignKey(Sellers, on_delete=models.CASCADE)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    amount = models.PositiveIntegerField()
    request_time = models.DateTimeField(default=now)



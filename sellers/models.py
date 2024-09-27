import uuid
from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User

class Sellers(models.Model):
    id = models.UUIDField(auto_created=True, primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(null=True, blank=True,max_length=30)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    registration_date =  models.DateTimeField(default=now, blank=True, editable=False)
    inventory = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)


    def increase_inventory(self, amount_to_increase):  
        if amount_to_increase <= 0:  
            raise ValueError("Amount must be a positive integer.")  
        self.inventory += amount_to_increase  
        self.save()

    def decrease_inventory(self, amount_to_decrease):  
        if amount_to_decrease <= 0:  
            raise ValueError("Amount must be a positive integer.")
        if self.inventory - amount_to_decrease < 0:
            raise ValueError("Inventory is Not Enough")
        self.inventory -= amount_to_decrease  
        self.save()

    def has_open_charge_request(self):
        open_charge_request_count = Charge.objects.filter(seller=self, is_confirmed=False).count()
        if open_charge_request_count:
            return True
        return False

class Charge(models.Model):
    id = models.UUIDField(auto_created=True, primary_key=True, default=uuid.uuid4, editable=False)
    seller = models.ForeignKey(Sellers, on_delete=models.CASCADE)
    amount = models.PositiveIntegerField()
    request_time = models.DateTimeField(default=now, blank=True, editable=False)
    confirmed_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    confirmed_time = models.DateTimeField(blank=True, null=True)
    is_confirmed = models.BooleanField(default=False)



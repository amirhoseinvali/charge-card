import uuid
from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User

class Sellers(models.model):
    id = models.UUIDField(auto_created=True, primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(null=True, blank=True,max_length=30)
    registration_date =  models.DateTimeField(default=now, blank=True, editable=False)
    inventory = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)




class Charge(models.Model):
    id = models.UUIDField(auto_created=True, primary_key=True, default=uuid.uuid4, editable=False)
    seller = models.ForeignKey(Sellers, on_delete=models.CASCADE)
    amount = models.PositiveIntegerField(default=0)
    request_time = models.DateTimeField(default=now, blank=True, editable=False)
    confirmed_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    confirmed_time = models.DateTimeField(blank=True, null=True)
    is_confirmed = models.BooleanField(default=False)

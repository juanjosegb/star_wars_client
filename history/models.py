from django.contrib.auth.models import User
from django.db import models


class History(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    page = models.CharField(max_length=32)
    created_at = models.DateField(auto_now_add=true)

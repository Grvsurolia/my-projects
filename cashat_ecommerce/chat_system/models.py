from django.db import models
from ecommerce_users.models import User

# Create your models here.

class Chat(models.Model):
    from_user = models.ForeignKey(User,on_delete=models.CASCADE, related_name = 'From_user')
    to_user = models.ForeignKey(User,on_delete=models.CASCADE, related_name = 'To_user')
    message = models.TextField()


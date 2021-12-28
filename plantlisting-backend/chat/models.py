from django.db import models
from django.db.models import Q
from django.utils.translation import ugettext_lazy as _
from CustomUserModel.models import CustomUser
from django.utils.safestring import mark_safe


class PersonManager(models.Manager):
    def get_or_new(self,me,other):
        if str(me) == str(other):
            return None
        u1 = CustomUser.objects.get(username=me)
        u2 = CustomUser.objects.get(username=other)
        qs = ChatUser.objects.filter(Q(Q(user1=u2) & Q(user2=u1)) | Q(Q(user1=u1) & Q(user2=u2)))
        if qs.count() >= 1:
            return qs
        else:
            if me != other:
                obj = ChatUser.objects.create(user1=u1,user2=u2)
                return obj,True
            None,False
            

class ChatUser(models.Model):
    user1 = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    user2 = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='user2')
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    objects = PersonManager()
    
    def __str__(self):
        return f'{self.pk}'
    
    class Meta:
        ordering = ['timestamp']
        
    def get_user(self):
        return self.user1 + ' with ' + self.user2 
    

class Message(models.Model):
    person = models.ForeignKey(ChatUser, on_delete=models.CASCADE, blank=True, null=True)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='user')
    message = models.TextField(blank=True,null=True)
    image_base64 = models.ImageField(blank=True,null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self):
        return str(self.user)
    
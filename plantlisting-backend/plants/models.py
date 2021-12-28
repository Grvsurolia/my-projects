from django.db import models
from CustomUserModel.models import CustomUser
from django.utils.translation import ugettext_lazy as _

class PlantType(models.Model):
    name = models.CharField(max_length=150)
    # datetime = models.DateTimeField(auto_now=False, auto_now_add=False)
    def __str__(self):
        return str(self.name)

    def get_name(self):
        return self.name



STATUS = (
       ('available', ('AVAILABLE')),
       ('taken', ('TAKEN')),
       ('not_available', ('NOT_AVAILABLE')),
   )
class Plant(models.Model):
    plant_name = models.CharField(max_length=255)
    plant_type = models.ManyToManyField(PlantType)
    other_p_type = models.CharField(plant_type, blank=True, null=True, max_length=255)
    description=models.TextField()
    quantity = models.IntegerField(blank=False, null=False)
    city = models.CharField(max_length=255, blank=True, null=True,)
    img1 = models.ImageField(upload_to='upload/', height_field=None, width_field=None, max_length=None,blank = True, null = True)
    img2 = models.ImageField(upload_to='upload/', height_field=None, width_field=None, max_length=None,blank = True, null = True)
    img3 = models.ImageField(upload_to='upload/', height_field=None, width_field=None, max_length=None,blank = True, null = True)
    img4 = models.ImageField(upload_to='upload/', height_field=None, width_field=None, max_length=None,blank = True, null = True)
    status = models.CharField(max_length=32,choices=STATUS,default='available',blank = True, null = True)
    owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    datetime = models.DateField(auto_now=True)

    def __str__(self):
        return self.plant_name
    
    
    def get_plantname(self):
        return self.plant_name + ' is ' + self.description
    
    @property
    def owner_name(self):
        return self.owner.username
    
   
class WishList(models.Model):
    user_id = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    plant_id = models.ForeignKey(Plant, on_delete=models.CASCADE)
    add_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.user_id.username
    

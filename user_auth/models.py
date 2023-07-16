from django.db import models
from django.contrib.auth.models import User
from local_validation import newPasswordValidator
from django.contrib.auth import password_validation
from django.core.validators import validate_image_file_extension
# Create your models here.

class PersonalInfo(User):
    User.email = models.EmailField(unique=True)
    User.password= models.CharField(validators=[password_validation,newPasswordValidator],)
    
    """This is a STI (Single table inheritance) model of the built-in User model.
    It is different from the user profile, 
    as it only contains  few details from the User model """
    def __str__(self) -> str:
        return self.username

class UserProfile(PersonalInfo):
    """ Additioinal info about the user"""
    is_customer = models.BooleanField(default=True)
    picture = models.ImageField(null=True, blank=True, validators=[validate_image_file_extension])
    contact = models.CharField(max_length=20, null=True, unique=True,)
    
    
    def __str__(self) -> str:
        return self.username
    class Meta:
        ordering =['-id']



class UserLocation(models.Model):
    """The user's location information, starting from country, down to 
    home address."""
    individual = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='address')
    address = models.CharField(max_length=200,)
    city = models.CharField(max_length=100,)
    state = models.CharField(max_length=50)
    country = models.CharField(max_length=100)
    zip_code = models.PositiveBigIntegerField(null=True, blank=True)

    def __str__(self) -> str:
        return self.individual.username+" "+self.address
    
    class Meta:
        ordering = ['individual']

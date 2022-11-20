from django.db import models
from django.contrib.auth.models import User
from versatileimagefield.fields import VersatileImageField
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField


# Create your models here.


class ProfileImg(models.Model):
    user = models.OneToOneField(User,null=True, on_delete=models.CASCADE)
    profileimg = VersatileImageField(upload_to='profile',default='prifiledummy.png')


    def __str__(self):
        return self.user.username


class Blog(models.Model):
    title = models.CharField(max_length=250,null=True)
    description = models.CharField(max_length=1000,null=True)
    detailDiscription = RichTextUploadingField(blank=True,null=True)
    place =  models.CharField(max_length=300,null=True)
    date = models.DateTimeField(auto_now_add=True,null=True)
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    cover_image = VersatileImageField(upload_to='web',default='default.jpg')
    twoimage = VersatileImageField(upload_to='web',default='default.jpg')
    threeimage = VersatileImageField(upload_to='web',default='default.jpg')

    def __str__(self):
        return self.title

class Hotel(models.Model):
    name=models.CharField(max_length=200)
    place=models.CharField(max_length=200)
    image=models.ImageField(null=True, blank=True)
    description=models.TextField(max_length=1000)
    roomtype=models.CharField(max_length=200)
    count=models.IntegerField(null=True)
    rate=models.FloatField(max_length=200)
    available_rooms=models.IntegerField(null=True)

    def __str__(self):
        return self.name


class Booking(models.Model):
    room_count=models.IntegerField(null=True)
    rate=models.FloatField(max_length=200, null=True, blank=True)
    hotel=models.ForeignKey(Hotel,on_delete=models.CASCADE)
    check_in=models.DateField(null=True)
    check_out=models.DateField(null=True)
    name=models.CharField(max_length=200)
    phone=models.IntegerField(null=True)

    
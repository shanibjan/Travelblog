from django.urls import path
from . import views




urlpatterns = [
    path('',views.about, name="home"),
    path('blog/',views.index,name="index"),
    path('hotels/',views.hotels,name="hotels"),
    path('hotel_booking/<str:pk>/',views.booking, name="booking"),
    path('detail/<str:pk>/',views.blogdetails, name="blogdetail"),
    path('profile/<str:user>/',views.profile,name="profile"),
  

    path('cretepost/',views.createpost,name='createpost'),
    path('updatepost/<str:pk_update>/',views.updatepost,name="updatepost"),
    path('delete/<str:pk_del>/',views.deletepost,name="deletepost"),

    path('editprofile/',views.editprofile,name = "editprofile"),
    path('editimg/',views.editimg,name="editimg"),

    path('login/',views.loginpage,name="login"),
    path('registration/',views.registrationpage,name="registration"),
    path('logout/',views.logoutpage,name='logout')
]
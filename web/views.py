from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Blog, User, Hotel
from django.contrib.auth.forms import UserCreationForm
from .form import UserRegisterForm, PostBlog, UserProfile, Useredit, Booking
from django.contrib import messages
from django.contrib.auth import authenticate,   login, logout 
from django.contrib.auth.decorators import login_required
from .filters import ProfileFilter,PostFilter
from django.db.models import Q

def index(request):
   posts = Blog.objects.order_by('-id')
   authors = User.objects.all()
   myfilter = PostFilter(request.GET,queryset=posts)
   posts = myfilter.qs
   # user = posts.user_set.all()
   context = {
      'posts':posts,
      'myfilter':myfilter,
      'authors':authors
      # 'user':user
   }
   return render(request,'index.html',context)

def hotels(request):
   hotels = Hotel.objects.all()
   q = request.GET.get('search')
   if q is not None:
      hotels = Hotel.objects.filter(Q(name__icontains=q) | Q(place__icontains=q))
   context = {
      'hotels':hotels
   }
   return render(request,'hotels.html',context)

def booking(request,pk):
   hotel = Hotel.objects.get(pk=pk)
   form = Booking()
   if request.method == 'POST':
      form = Booking(request.POST,request.FILES)
      form.instance.user = request.user
      form.instance.hotel = hotel
      if form.is_valid():
         form.save()
         messages.success(request, 'Booking completed')
         return redirect('hotels')
   context = {
      'hotel':hotel,
      'form':form
   }
   return render(request,'hotel_booking.html',context) 

def blogdetails(request,pk):
   posts = Blog.objects.get(id=pk)
   context = {
      'posts':posts
   }
   return render(request,'blog_detail.html',context)


def about(request):
   return render(request,'home.html')




def loginpage(request):
   if request.user.is_authenticated:
      return redirect('index')
   else:
      if request.method == 'POST':
         username = request.POST.get('username')
         password = request.POST.get('password')
         user = authenticate(request,username=username,password=password)
         if user is not None:
            login(request,user)
            return redirect('index')

      return render(request,'login.html')




def registrationpage(request):
   if request.user.is_authenticated:
      return redirect('index')
   else:
      form = UserRegisterForm()
      if request.method == 'POST':
         form = UserRegisterForm(request.POST)
         if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request,'user created for '+ user)
            return redirect('login')

      context = {
         'form' : form
      }
      return render(request,'registration.html',context)



def logoutpage(request):
   logout(request)
   return redirect('login')

   
@login_required(login_url='login')
def profile(request,user):
   user = User.objects.get(id=user)
   posts = user.blog_set.all()
   total_posts = posts.count()
   myfilters = ProfileFilter(request.GET,queryset = posts)
   posts = myfilters.qs
   context = {
      'user':user,
      'posts':posts,
      'total_posts': total_posts,
      'myfilters':myfilters
   }
   return render(request,'profile.html',context)

@login_required(login_url='login')
def editprofile(request):
   form = Useredit(instance=request.user)
   if request.method == 'POST':
      form = Useredit(request.POST,instance=request.user)
      user_id = request.user.id
      if form.is_valid():
         form.save()
         return redirect('/profile/{}/'.format(user_id))
   context = {
      'form':form,
      
   }
   return render(request,'editprofile.html',context)


@login_required(login_url='login')
def editimg(request):
   form = UserProfile(instance=request.user.profileimg)
   if request.method == 'POST':
      form = UserProfile(request.POST,request.FILES,instance=request.user.profileimg)
      form.instance.user = request.user
      user_id = request.user.id
      if form.is_valid():
         form.save()
         return redirect('/profile/{}/'.format(user_id))
   context = {
      'form':form
   }
   return render(request,'editimg.html',context)

@login_required(login_url='login')
def createpost(request):
   form = PostBlog()
   if request.method == 'POST':
      form = PostBlog(request.POST,request.FILES)
      form.instance.user = request.user
      if form.is_valid():
         form.save()
         return redirect('index')

   context = {
      'form':form
   }
   return render(request,'createpost.html',context)




def updatepost(request,pk_update):
   post = Blog.objects.get(id=pk_update)
   form = PostBlog(instance=post)
   user_id = request.user.id
   if request.method == 'POST':
      form = PostBlog(request.POST,request.FILES,instance=post)
      if form.is_valid():
         form.save()
         return redirect('/profile/{}/'.format(user_id))
   context = {
      'form':form
   }
   return render(request,'createpost.html',context)


def deletepost(request,pk_del):
   post = Blog.objects.get(id=pk_del)
   user_id = request.user.id
   if request.method == 'POST':
      post.delete()
      return redirect('/profile/{}/'.format(user_id))
   context = {
      'item':post,
      'userid':user_id
   }
   return render(request,'delete.html',context)
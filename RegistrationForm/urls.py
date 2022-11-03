from django.contrib import admin
from django.urls import path
from enroll import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('registration', views.SignUp, name= 'signup'),
    path('login', views.Login, name= 'login'),
    path('profile', views.UserProfile, name= 'profile'),
    path('logout', views.LogOut, name= 'logout'),
    path('changepass', views.ChanagePassword, name= 'changepass'),
]

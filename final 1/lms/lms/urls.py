
from django.contrib import admin
from django.urls import path,include
from .import views,user_login

urlpatterns = [
    path('admin/', admin.site.urls),

    path('base',views.BASE,name='base'),

    path('',views.HOME,name='home'),

    path('single/course',views.SINGLE_COURSE, name='single_course'),

    path('contact', views.CONTACT_US, name='contact_us'),

    path('about', views.ABOUT_US, name='about_us'),

    path('accounts/register',user_login.REGISTER,name='register'),

    path('accounts/', include('django.contrib.auth.urls')),

    path('doLogin',user_login.DO_LOGIN,name='doLogin'),

    path('accounts/profile',user_login.PROFILE,name='profile'),

    path('accounts/profile/update',user_login.PROFILE_UPDATE,name='profile_update'),

]

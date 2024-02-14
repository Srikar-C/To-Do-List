from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name='home'),
    path('home',views.home,name='home'),
    path('login',views.login,name='login'),
    path('register',views.register,name='register'),
    path('loginDetails',views.loginDetails,name='loginDetails'),
    path('regDetails',views.regDetails,name='regDetails'),
    path('user',views.user,name='user'),
    path('userhome',views.user,name='user'),
    path('addItems',views.addItems,name='addItems'),
    path('addList',views.addList,name='addList'),
    path('viewlist',views.viewlist,name='viewlist'),
    path('modify',views.modify,name='modify'),
    path('delete',views.delete,name='delete'),

]
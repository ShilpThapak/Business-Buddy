from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('business-buddy', views.business_buddy, name="business-buddy"),
    path('business-buddy/login', views.login_view, name="login"),
    path('business-buddy/logout', views.logout_view, name="logout"),
    path('business-buddy/register',views.register, name="register"),
    path('business-buddy/sales', views.sales, name="sales"),
    path('business-buddy/sales/leadpage/<str:leadid>', views.leadpage, name="leadpage"),
    path('business-buddy/sales/assign', views.assign, name='assign'),
    path('savelead', views.savelead, name='savelead'),
    path('addactivity', views.addactivity, name='addactivity'),
    path('addtask', views.addtask, name='addtask'),
    path('taskdone', views.taskdone, name='taskdone'),
    path('business-buddy/sales/editstatus', views.editstatus, name='editstatus')
]
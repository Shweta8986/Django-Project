from django.contrib import admin
from django.urls import path,include
from myapp import views

urlpatterns = [
    path('contact/',views.contact,name='contact'),
    path('add_newmember/',views.add_newmember,name='add_newmember'),
    path('all_members/',views.all_members,name='all_members'),
    path('all_members/detail/<int:id>', views.detail, name='detail'),
    path('all_members/detail/update/<int:id>/',views.update,name='update'),
    path('all_members/detail/delete/<int:id>/',views.delete,name='delete'),
    path('testing/',views.testing,name='testing')
]

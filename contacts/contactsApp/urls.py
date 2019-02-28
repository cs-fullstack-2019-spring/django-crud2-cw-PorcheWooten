from django.urls import path
from . import views

urlpatterns= [

    path('',views.index, name='index'),
    path('contacts/',views.contacts, name='contacts'),
    path('contacts/edit/<int:id>/',views.editcontact, name='edit'),
    path('contacts/delete/<int:id>/',views.deletecontact, name='delete'),
]
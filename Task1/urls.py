from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomePage, name='home-page'),
    path('addprofile/',views.AddProfile, name='add-profile-page'),
    path('update/<str:pk>/',views.EditProfile, name='edit-profile-page'),
    path('delete/<str:pk>/',views.DeleteProfile, name='delete-profile-page')
]

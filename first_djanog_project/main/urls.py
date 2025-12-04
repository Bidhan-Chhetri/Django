from django.urls import path
from main import views 

urlpatterns = [
    path('home/', views.home),
    path('about/', views.about),
    path('contact/', views.contact),
    path('greet/', views.greet)
]

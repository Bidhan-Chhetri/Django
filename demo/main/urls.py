from django.urls import path
from main import views


urlpatterns = [
    path("home/", views.home, name="homepage"),
    path('about/', views.about, name="aboutpage"),
    path('contact/', views.contact, name="contactpage")
]
from django.urls import path
from .views import *

urlpatterns = [
    path('', HomeView, name="home"),
    path('about/', AboutView, name="about"),
    path('shop/', ShopView, name="shop"),
    path('services/', ServicesView, name="services"),
    path('blog/', BlogView, name="blog"),
    path('contact/', ContactView, name="contact"),
]




from django.urls import path

from . import views

urlpatterns = [
    path('', views.home_page, name='home_page'),
    path('login/', views.login, name='login'),
    path('registration/', views.registration, name='registration'),
# path('details', views.details, name='details'),

]
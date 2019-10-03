from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('login',views.login,name='login'),
    path('pricing',views.pricing,name='pricing'),
    path('trainers',views.trainers,name='trainers'),
    path('signup',views.signup,name='signup'),
    path('recepies',views.recepies,name='recepies'),
]

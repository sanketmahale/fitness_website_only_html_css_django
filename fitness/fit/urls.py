from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='home'),
    path('login',views.login,name='login'),
    path('pricing',views.pricing,name='pricing'),
    path('trainers',views.trainers,name='trainers'),
    path('signup',views.signup,name='signup'),
    path('recepies',views.recepies,name='recepies'),
    path('pay',views.pay,name='pay'),
    path('logout',views.logout,name='logout')
]

urlpatterns = urlpatterns + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

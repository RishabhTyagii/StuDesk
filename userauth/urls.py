from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView
from .views import signup,user_logout
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.user_login, name='login'),
    path('profile/', views.user_profile, name='profile'),
    path('logout/', user_logout, name='logout'), ]

urlpatterns += [
    path('signup/', signup, name='signup'),
        path('verify-otp/', views.verify_otp, name='verify_otp'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)




 
      # Your index page route
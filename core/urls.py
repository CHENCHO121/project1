from django.urls import path,include
from .import views


urlpatterns = [
    path('',views.home,name='home'),
    path('ContactMe',views.contact,name='contact'),
    path('Signup',views.Signup,name='register'),
    path('registration/', include('django.contrib.auth.urls')),
    path('profile',views.ProfileView,name='profile'),
    path('create',views.create_profile,name='create'),
    path('update',views.UpdateProfile, name='update'),
    path('oauth/', include('social_django.urls', namespace='social')),


]


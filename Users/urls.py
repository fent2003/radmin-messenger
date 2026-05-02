from django.urls import path
from Users import views

urlpatterns = [
    path("", views.profile, name='profile'),
    path("logout/", views.logout_profile, name='logout'),
    path('register/', views.RegisterUser.as_view(), name="register"),
    path('login/', views.LoginUser.as_view(), name='login'),

]
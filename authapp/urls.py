from django.urls import path, include
from authapp import views


urlpatterns = [
    path('signup/', views.signup, name="signup"),
    path('login/', views.handlelogin, name="handlelogin"),
    path('logout/', views.handlelogout, name="handlelogout"),
    path('profile/', views.user_profile_details, name='user_profile_details'),

]

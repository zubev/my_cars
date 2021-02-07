

from django.urls import path

from accounts.views import register, LogoutUserView,your_profile,show_profile,login_user

urlpatterns = [
    path('register/', register, name='register'),
    path('logout_user/', LogoutUserView.as_view(), name='user logout'),
    path('login/', login_user, name='login'),
    path('profile/<int:pk>', show_profile, name='profile'),
    path('profile/', your_profile, name='current profile'),
]

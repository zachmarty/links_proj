from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LoginView
from user.apps import UserConfig
from user.views import RegisterView, ProfileView, logout_view

app_name = UserConfig.name

urlpatterns = [
    path('login', LoginView.as_view(template_name = 'user/login.html'), name='login'),
    path('logout', logout_view, name = 'logout'),
    path('register', RegisterView.as_view(), name='register'),
    path('profile', ProfileView.as_view(), name='profile')
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

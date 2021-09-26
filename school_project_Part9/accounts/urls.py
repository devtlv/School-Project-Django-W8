from django.urls import path, include
from .views import SignUp, Register

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('signup/', SignUp.as_view(), name='signup'),
    path('register/', Register.as_view(), name='register')
]

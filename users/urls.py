from django.urls import path
from .views import RegisterView, LoginView, ProfileView

urlpatterns = [
    path('signup/', RegisterView.as_view()),
    path('signin/', LoginView.as_view()),
    path('me/', ProfileView.as_view()),
]

from django.urls import path
from knox import views as knox_views
from .views import AnswerView, RegistrationView, LoginAPIView

app_name = 'test_app'
urlpatterns = [
    path('registration/', RegistrationView.as_view(), name='registration'),
    path('login/', LoginAPIView.as_view(), name='login'),
    path('logout/', knox_views.LogoutView.as_view(), name='logout'),
    path('upload_answer/', AnswerView.as_view(), name='answer'),
]

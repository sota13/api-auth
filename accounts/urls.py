from django.urls import path
from .views import MyTokenObtainPairView, registerUser, getUsers


urlpatterns = [
    path('login/', MyTokenObtainPairView.as_view()),
    path('register/', registerUser),
    path('', getUsers),

]

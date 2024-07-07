from rest_framework.authtoken.views import obtain_auth_token
from django.urls import path
from .views import UserCreate, UserDelete, Logout

urlpatterns = [
    path('login/', obtain_auth_token),
    path('create/', UserCreate.as_view() ),
    path('logout/', Logout.as_view() ),
    path('delete/<int:pk>', UserDelete.as_view()),

]

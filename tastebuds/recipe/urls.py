"""
URL configuration for tastebuds project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from .views import RecipeList, RecipeDetail, CommentList, CommentDetail, CommentCreate, RecipeCreate, LikeCreate, LikeList, LikeDetail, RecipeUpdate, RecipeDelete

urlpatterns = [
    path('admin/', admin.site.urls),
    path('list/', RecipeList.as_view()),
    path('create/', RecipeCreate.as_view()),
    path('<int:pk>', RecipeDetail.as_view()),
    path('update/<int:pk>', RecipeUpdate.as_view()),
    path('delete/<int:pk>', RecipeDelete.as_view()),
    path('<int:pk>/comments-create', CommentCreate.as_view()),
    path('<int:pk>/comments', CommentList.as_view()),
    path('comments/<int:pk>', CommentDetail.as_view()),
    path('<int:pk>/likes-create', LikeCreate.as_view()),
    path('<int:pk>/likes', LikeList.as_view()),
    path('likes/<int:pk>', LikeDetail.as_view())
]

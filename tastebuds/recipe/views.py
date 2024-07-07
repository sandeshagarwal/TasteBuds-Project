from django.shortcuts import render
from .models import Recipe, Comment, Like
from rest_framework.views import APIView
from .serializers import RecipeSerializer, CommentSerializer, LikeSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from rest_framework.exceptions import ValidationError
from .permissions import AdminOrReadOnly, RecipeAuthorAndAdminOrReadOnly, CommentAuthorAndAdminOrReadOnly, LikeAuthorOrReadOnly
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from .pagination import RecipePagination

class RecipeList(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    pagination_class = RecipePagination
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
    
class RecipeCreate(generics.CreateAPIView):
    permission_classes =[IsAuthenticated]
    serializer_class = RecipeSerializer
    
    def perform_create(self, serializer):
        author_id = self.request.user
        serializer.save(author_id=author_id)
    

class RecipeDetail(generics.RetrieveAPIView):
    permission_classes =[IsAuthenticated]
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer

class RecipeUpdate(generics.UpdateAPIView):
    permission_classes = [RecipeAuthorAndAdminOrReadOnly]
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
    
class RecipeDelete(generics.DestroyAPIView):
    permission_classes = [RecipeAuthorAndAdminOrReadOnly]
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
    
class CommentList(generics.ListAPIView): # need to get specific comments for a recipe
    serializer_class = CommentSerializer
    
    def get_queryset(self):
        pk = self.kwargs['pk']
        return Comment.objects.filter(recipe=pk)
    
class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [CommentAuthorAndAdminOrReadOnly]
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    
class CommentCreate(generics.CreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = CommentSerializer
    
    def perform_create(self, serializer):
        pk = self.kwargs.get('pk')
        recipe_object = Recipe.objects.get(pk=pk)
        
        comment_author_object = self.request.user
        
        serializer.save(recipe=recipe_object, comment_author=comment_author_object)
        

        
class LikeList(generics.ListAPIView): # need to get specific Likes for a recipe
    serializer_class = LikeSerializer
    
    def get_queryset(self):
        pk = self.kwargs['pk']
        return Like.objects.filter(recipe=pk)
    
class LikeDetail(generics.RetrieveDestroyAPIView):
    permission_classes = [LikeAuthorOrReadOnly]
    queryset = Like.objects.all()
    serializer_class = LikeSerializer
    
class LikeCreate(generics.CreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = LikeSerializer
    
    def perform_create(self, serializer):
        pk = self.kwargs.get('pk')
        recipe_object = Recipe.objects.get(pk=pk)
        
        like_author_object = self.request.user
    
        like_queryset = Like.objects.filter(recipe=recipe_object, like_author=like_author_object)

        if like_queryset.exists():
            raise ValidationError("You have already liked this recipe!")

        
        serializer.save(recipe=recipe_object, like_author=like_author_object)
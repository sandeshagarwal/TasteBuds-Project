from rest_framework import serializers
from .models import Recipe, Comment, Like

class CommentSerializer(serializers.ModelSerializer):
    comment_author = serializers.StringRelatedField(read_only=True)
    
    class Meta:
        model = Comment
        exclude = ['recipe']
        
class LikeSerializer(serializers.ModelSerializer):
    like_author = serializers.StringRelatedField(read_only=True)
    class Meta:
        model = Like
        exclude = ['recipe']


class RecipeSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(read_only=True, many=True)
    likes = LikeSerializer(read_only=True, many=True)
    author_id = serializers.StringRelatedField(read_only=True)
    class Meta:
        model = Recipe
        fields = '__all__'




# class RecipeSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     author_id = serializers.CharField()
#     title = serializers.CharField()
#     description = serializers.CharField()
#     created_at = serializers.DateTimeField()
#     ingredients = IngredientSerializer(read_only=True, many=True)
#     instructions = serializers.CharField()

#     def create(self, validated_data):
#         """
#         Create and return a new `Snippet` instance, given the validated data.
#         """
#         return Recipe.objects.create(**validated_data)
    
#     def update(self, instance, validated_data):
#         """
#         Update and return an existing `Snippet` instance, given the validated data.
#         """
#         instance.title = validated_data.get('title', instance.title)
#         instance.description = validated_data.get('description', instance.description)
#         instance.save()
#         return instance
    

    
from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Recipe(models.Model):
    author_id = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100, null=True, blank=True, default=None)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    ingredients = models.TextField()
    instructions = models.TextField()
    
    def __str__(self):
        return self.title
    
class Comment(models.Model):
    desc = models.TextField()
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name="comments")
    comment_author = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.recipe.title
    
class Like(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name="likes")
    like_author = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.recipe.title

    

from rest_framework import serializers
from .models import Author, Article, Comment, Tag

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'

class ArticleSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, required=False)
    tags = TagSerializer(many=True, required=False)
    class Meta:
        model = Article
        fields = '__all__'

from rest_framework import serializers
from .models import Author, Article, Comment, Tag
from rest_framework_bulk import (
    BulkListSerializer,
    BulkSerializerMixin,
)

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'

class AuthorBulkSerializer(BulkSerializerMixin, serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'
        list_serializer_class = BulkListSerializer

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'
        depth = 0

class ArticleIncludeAllSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, required=False)
    tags = TagSerializer(many=True, required=False)
    class Meta:
        model = Article
        fields = ("id", "author", "title", "content", "comments", "tags")
        depth = 3

from django.shortcuts import render
from rest_framework import generics
from rest_framework import viewsets
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Author, Article, Comment, Tag
from .serializers import AuthorSerializer, AuthorBulkSerializer, ArticleIncludeAllSerializer, ArticleSerializer, CommentSerializer, TagSerializer
from rest_framework_bulk import (
    ListBulkCreateUpdateDestroyAPIView,
    BulkModelViewSet
)

class ListAuthorView(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

class ListAuthorBulkView(BulkModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorBulkSerializer

class ListArticleView(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

class ListArticleIncludeAllView(viewsets.ReadOnlyModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleIncludeAllSerializer

class ListCommentView(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

class ListTagView(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer

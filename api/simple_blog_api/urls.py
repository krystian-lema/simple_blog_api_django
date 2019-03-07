from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
# router.register('authors', views.ListAuthorView)
# router.register('articles', views.ListArticleView)
# router.register('articles_include_all', views.ListArticleIncludeAllView)
# router.register('comments', views.ListCommentView)
# router.register('tags', views.ListTagView)

urlpatterns = [
    path('', include(router.urls))
]

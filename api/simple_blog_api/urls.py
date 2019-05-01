from django.urls import path, include
from . import views
from rest_framework import routers
from rest_framework_bulk.routes import BulkRouter

router = routers.DefaultRouter()
router.register('authors', views.ListAuthorView)
router.register('articles', views.ListArticleView)
router.register('articles_include_all', views.ListArticleIncludeAllView)
router.register('comments', views.ListCommentView)
router.register('tags', views.ListTagView)

bulk_router = BulkRouter()
bulk_router.register(r'authors_bulk', views.ListAuthorBulkView)

urlpatterns = [
    path('', include(router.urls)),
    path('', include(bulk_router.urls))
]

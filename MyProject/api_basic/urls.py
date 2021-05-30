from django.urls import path, include
from .views import article_list, article_detail, ArticleAPIView, ArticleDetails, GenericAPIView, ArticleViewSet

from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(prefix="article", viewset=ArticleViewSet, basename="article")

urlpatterns = [
    # path("article/", article_list),
    path("article/", ArticleAPIView.as_view()),
    # path("detail/<int:pk>/", article_detail)
    path("detail/<int:id>/", ArticleDetails.as_view()),
    path("generic/article/<int:id>/", GenericAPIView.as_view()),

    path("viewset/", include(router.urls)),
]

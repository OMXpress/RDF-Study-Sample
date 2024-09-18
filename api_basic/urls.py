from django.urls import path, include
from .views import ArticleViewSet,ArticleApiView, ArticleDetails, GenereicAPIView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('article', ArticleViewSet, basename='article')

urlpatterns = [
    path('viewset/', include(router.urls)),
    path('viewset/<int:pk>', include(router.urls)),
    path('article/', ArticleApiView.as_view()),
    path('detail/<int:id>/', ArticleDetails.as_view()),
    path('generic/article/<int:id>/', GenereicAPIView.as_view()),
    path('generic/article/', GenereicAPIView.as_view())
]

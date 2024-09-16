from django.urls import path
from .views import ArticleApiView, ArticleDetails, GenereicAPIView

urlpatterns = [
    path('article/', ArticleApiView.as_view()),
    path('detail/<int:id>/', ArticleDetails.as_view()),
    path('generic/article/<int:id>/', GenereicAPIView.as_view()),
    path('generic/article/', GenereicAPIView.as_view())
]

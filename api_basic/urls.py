from django.urls import path
from .views import ArticleApiView, ArticleDetails

urlpatterns = [
    path('article/', ArticleApiView.as_view()),
    path('detail/<int:pk>/', ArticleDetails.as_view())
]

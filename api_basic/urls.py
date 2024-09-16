from django.urls import path
from .views import article_list, article_details, ArticleApiView

urlpatterns = [
    # path('article/', article_list),
    path('article/', ArticleApiView.as_view()),
    path('detail/<int:pk>/', article_details)
]

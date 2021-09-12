from django.urls import path
from django.urls.resolvers import URLPattern

from .views import ArticleListView, ArticleDetailView

urlpatterns = [
    path('', ArticleListView.as_view()),
    path('<pk>', ArticleDetailView.as_view()),
]



from django.urls import path, re_path,include
from apps.news.views import *

urlpatterns = [
    path('all/', NewsView.as_view(), name='all'),
    path('detail/<int:news_id>/', NewsDetails.as_view(), name='news_detail'),
]
from django.urls import path, re_path
from . import views


urlpatterns = [
    path('', views.IndexView.as_view(), name='home'),
    re_path(r'^(?P<path>.*)/$', views.IndexView.as_view()),
]

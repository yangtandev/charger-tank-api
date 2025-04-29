from django.urls import path
from . import views

urlpatterns = [
    path('', views.ClientSettingListView.as_view()),
    path('<str:pk>/', views.ClientSettingDetailView.as_view()),
]

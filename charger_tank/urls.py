from django.urls import path
from . import views

urlpatterns = [
    # Current
    path('current/', views.ChargerTankCurrentListCreateView.as_view()),
    path('current/<int:pk>/', views.ChargerTankCurrentDetailView.as_view()),

    # History
    path('history/', views.ChargerTankHistoryListCreateView.as_view()),
    path('history/<int:pk>/', views.ChargerTankHistoryDetailView.as_view()),

    # Status
    path('status/', views.ChargerTankStatusListCreateView.as_view()),
    path('status/<int:pk>/', views.ChargerTankStatusDetailView.as_view()),
]

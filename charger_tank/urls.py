from django.urls import path
from . import views

urlpatterns = [
    # Current
    path('current/', views.ChargerTankCurrentListCreateView.as_view()),
    path('current/<int:pk>/', views.ChargerTankCurrentDetailView.as_view()),

    # History
    path('history/', views.ChargerTankHistory5MinListCreateView.as_view()),
    path('history/<int:pk>/', views.ChargerTankHistory5MinDetailView.as_view()),

    # Status
    path('status/', views.ChargerTankStatusListCreateView.as_view()),
    path('status/<int:pk>/', views.ChargerTankStatusDetailView.as_view()),

    # Status History
    path('status-history/', views.ChargerTankStatusHistoryListCreateView.as_view()),
    path('status-history/<int:pk>/', views.ChargerTankStatusHistoryDetailView.as_view()),
]

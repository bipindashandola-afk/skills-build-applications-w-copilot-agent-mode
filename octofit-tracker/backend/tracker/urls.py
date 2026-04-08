from django.urls import path

from . import views

urlpatterns = [
    path('', views.tracker_root, name='tracker-root'),
    path('health/', views.health_check, name='tracker-health'),
]

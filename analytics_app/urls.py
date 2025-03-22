from django.urls import path
from . import views

urlpatterns = [
    path('analytics', views.analytics_view, name='analytics'),
    path('ask', views.ask_view, name='ask'),
    path('health', views.health_view, name='health'),
]

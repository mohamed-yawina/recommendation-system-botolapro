from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import LoginView, PlayerViewSet, RecommendationView

router = DefaultRouter(trailing_slash=False)
router.register(r'players', PlayerViewSet, basename='players')

urlpatterns = [
    path('auth/login', LoginView.as_view(), name='login'),
    path('recommendations/<str:player_id>', RecommendationView.as_view(), name='recommendations'),
    path('', include(router.urls)),
]
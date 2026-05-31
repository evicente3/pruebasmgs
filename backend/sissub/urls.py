from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'users', views.UserProfileViewSet, basename='user')
router.register(r'categories', views.CategoryViewSet, basename='category')
router.register(r'services', views.ServiceViewSet, basename='service')
router.register(r'currencies', views.CurrencyViewSet, basename='currency')
router.register(r'subscriptions', views.SubscriptionViewSet, basename='subscription')
router.register(r'subscription-users', views.SubscriptionUserViewSet, basename='subscription-user')

urlpatterns = [
    path('', include(router.urls)),
]

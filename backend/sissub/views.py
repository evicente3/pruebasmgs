from rest_framework import viewsets, permissions
from django.db.models import Prefetch

from .models import (
    UserProfile, Category, Service, Currency,
    Subscription, SubscriptionUser,
)
from .serializers import (
    UserProfileSerializer, CategorySerializer, ServiceSerializer,
    CurrencySerializer,
    SubscriptionReadSerializer, SubscriptionWriteSerializer,
    SubscriptionUserReadSerializer, SubscriptionUserWriteSerializer,
    UserProfileDetailSerializer, SubscriptionDetailSerializer,
)


class UserProfileViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.AllowAny]
    lookup_field = 'pk'

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return UserProfileDetailSerializer
        return UserProfileSerializer

    def get_queryset(self):
        if self.action == 'retrieve':
            return UserProfile.objects.prefetch_related(
                Prefetch('subscription_set', queryset=Subscription.objects.select_related(
                    'service', 'category', 'currency'
                )),
                Prefetch('category_set', queryset=Category.objects.all()),
            )
        return UserProfile.objects.all()


class CategoryViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.AllowAny]
    serializer_class = CategorySerializer

    def get_queryset(self):
        return Category.objects.all()


class ServiceViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.AllowAny]
    serializer_class = ServiceSerializer

    def get_queryset(self):
        return Service.objects.all()


class CurrencyViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.AllowAny]
    serializer_class = CurrencySerializer

    def get_queryset(self):
        return Currency.objects.all()


class SubscriptionViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.AllowAny]

    def get_serializer_class(self):
        if self.action in ('create', 'update', 'partial_update'):
            return SubscriptionWriteSerializer
        if self.action == 'retrieve':
            return SubscriptionDetailSerializer
        return SubscriptionReadSerializer

    def get_queryset(self):
        qs = Subscription.objects.select_related(
            'service', 'category', 'currency'
        )
        if self.action == 'retrieve':
            qs = qs.prefetch_related(
                Prefetch(
                    'subscriptionuser_set',
                    queryset=SubscriptionUser.objects.select_related('user'),
                )
            )
        return qs


class SubscriptionUserViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.AllowAny]

    def get_serializer_class(self):
        if self.action in ('create', 'update', 'partial_update'):
            return SubscriptionUserWriteSerializer
        return SubscriptionUserReadSerializer

    def get_queryset(self):
        if self.action in ('list', 'retrieve'):
            return SubscriptionUser.objects.select_related(
                'subscription__service', 'user'
            )
        return SubscriptionUser.objects.all()

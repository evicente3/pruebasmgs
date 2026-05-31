from rest_framework import serializers
from .models import (
    UserProfile, Category, Service, Currency,
    Subscription, SubscriptionUser,
)


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['id', 'email', 'username', 'status']


class CategorySerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(
        queryset=UserProfile.objects.all()
    )

    class Meta:
        model = Category
        fields = ['id', 'user', 'name', 'status']


class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = ['id', 'name', 'is_custom', 'status']


class CurrencySerializer(serializers.ModelSerializer):
    class Meta:
        model = Currency
        fields = ['id', 'symbol', 'status']


class SubscriptionFlatSerializer(serializers.ModelSerializer):
    service_name = serializers.CharField(
        source='service.name', read_only=True
    )

    class Meta:
        model = Subscription
        fields = ['id', 'service_name', 'amount',
                  'billing_cycle', 'status']


class SubscriptionReadSerializer(serializers.ModelSerializer):
    user_id = serializers.UUIDField(read_only=True)
    service = ServiceSerializer(read_only=True)
    category = CategorySerializer(read_only=True)
    currency = CurrencySerializer(read_only=True)

    class Meta:
        model = Subscription
        fields = [
            'id', 'user_id', 'service', 'category', 'currency',
            'amount', 'billing_cycle', 'next_billing_date', 'status',
            'created', 'modified',
        ]


class SubscriptionWriteSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(
        queryset=UserProfile.objects.all()
    )
    service = serializers.PrimaryKeyRelatedField(
        queryset=Service.objects.all()
    )
    category = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(),
        required=False, allow_null=True,
    )
    currency = serializers.PrimaryKeyRelatedField(
        queryset=Currency.objects.all()
    )

    class Meta:
        model = Subscription
        fields = [
            'user', 'service', 'category', 'currency',
            'amount', 'billing_cycle', 'next_billing_date', 'status',
        ]


class SubscriptionUserReadSerializer(serializers.ModelSerializer):
    user = UserProfileSerializer(read_only=True)
    subscription = SubscriptionFlatSerializer(read_only=True)

    class Meta:
        model = SubscriptionUser
        fields = ['id', 'subscription', 'user',
                  'percentage', 'status']


class SubscriptionUserWriteSerializer(serializers.ModelSerializer):
    subscription = serializers.PrimaryKeyRelatedField(
        queryset=Subscription.objects.all()
    )
    user = serializers.PrimaryKeyRelatedField(
        queryset=UserProfile.objects.all()
    )

    class Meta:
        model = SubscriptionUser
        fields = ['subscription', 'user', 'percentage', 'status']


class UserProfileDetailSerializer(serializers.ModelSerializer):
    subscriptions = SubscriptionReadSerializer(
        many=True, read_only=True, source='subscription_set'
    )
    categories = CategorySerializer(
        many=True, read_only=True, source='category_set'
    )

    class Meta:
        model = UserProfile
        fields = [
            'id', 'email', 'username', 'status',
            'subscriptions', 'categories',
        ]


class SubscriptionDetailSerializer(serializers.ModelSerializer):
    user_id = serializers.UUIDField(read_only=True)
    service = ServiceSerializer(read_only=True)
    category = CategorySerializer(read_only=True)
    currency = CurrencySerializer(read_only=True)
    subscription_users = SubscriptionUserReadSerializer(
        many=True, read_only=True, source='subscriptionuser_set'
    )

    class Meta:
        model = Subscription
        fields = [
            'id', 'user_id', 'service', 'category', 'currency',
            'amount', 'billing_cycle', 'next_billing_date', 'status',
            'created', 'modified', 'subscription_users',
        ]

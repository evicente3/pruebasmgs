from django.contrib import admin
from .models import UserProfile, Currency, Service, Category, Subscription, SubscriptionUser

@admin.register(UserProfile)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'email', 'username', 'status', 'created')
    search_fields = ('email', 'username')
    list_filter = ('status',)

@admin.register(Currency)
class CurrencyAdmin(admin.ModelAdmin):
    list_display = ('id', 'symbol', 'status')
    search_fields = ('id',)

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'is_custom', 'status')
    list_filter = ('is_custom', 'status')
    search_fields = ('name',)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'user', 'status')
    search_fields = ('name',)

@admin.register(Subscription)
class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'service', 'amount', 'currency', 'billing_cycle', 'next_billing_date', 'status')
    list_filter = ('status', 'billing_cycle', 'currency')
    date_hierarchy = 'next_billing_date'

@admin.register(SubscriptionUser)
class SubscriptionUserAdmin(admin.ModelAdmin):
    list_display = ('id', 'subscription', 'user', 'percentage', 'status')
    list_filter = ('status',)

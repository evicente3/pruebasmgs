from django.contrib import admin

from django.contrib import admin
from .models import UserProfile, Currency, Service, Category, Subscription, SubscriptionUser

admin.site.register(UserProfile)
admin.site.register(Currency)
admin.site.register(Service)
admin.site.register(Category)
admin.site.register(Subscription)
admin.site.register(SubscriptionUser)

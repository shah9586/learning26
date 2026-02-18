from django.contrib import admin
from .models import Product, Nutrition, HealthScore, Reward, ScanHistory


# 🔹 Nutrition Inline (Shows inside Product)
class NutritionInline(admin.StackedInline):
    model = Nutrition
    extra = 0


# 🔹 Health Score Inline
class HealthScoreInline(admin.StackedInline):
    model = HealthScore
    extra = 0


# 🔹 Product Admin
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_name', 'brand_name', 'category', 'barcode')
    search_fields = ('product_name', 'brand_name', 'barcode')
    list_filter = ('category',)
    inlines = [NutritionInline, HealthScoreInline]


# 🔹 Reward Admin
@admin.register(Reward)
class RewardAdmin(admin.ModelAdmin):
    list_display = ('user', 'points', 'activity', 'created_at')
    list_filter = ('activity',)
    search_fields = ('user__username',)


# 🔹 Scan History Admin
@admin.register(ScanHistory)
class ScanHistoryAdmin(admin.ModelAdmin):
    list_display = ('user', 'product', 'scanned_at')
    search_fields = ('user__username', 'product__product_name')
    list_filter = ('scanned_at',)

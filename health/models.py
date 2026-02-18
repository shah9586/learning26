

# Create your models here.
from django.db import models
from django.contrib.auth.models import User


class Product(models.Model):
    product_name = models.CharField(max_length=200)
    brand_name = models.CharField(max_length=150)
    barcode = models.CharField(max_length=50, unique=True)
    category = models.CharField(max_length=100)
    serving_size = models.CharField(max_length=50)
    image = models.ImageField(upload_to='products/', null=True, blank=True)

    def __str__(self):
        return self.product_name
    
    class Meta:
        db_table = 'health_product'


class Nutrition(models.Model):
    product = models.OneToOneField(Product, on_delete=models.CASCADE)
    calories = models.FloatField()
    protein = models.FloatField()
    carbohydrates = models.FloatField()
    sugar = models.FloatField()
    fat = models.FloatField()
    sodium = models.FloatField()
    fiber = models.FloatField()

    def __str__(self):
        return f"Nutrition - {self.product.product_name}"
    class Meta:
        db_table = 'health_nutrition'


class HealthScore(models.Model):
    product = models.OneToOneField(Product, on_delete=models.CASCADE)
    score_percentage = models.IntegerField()
    score_reason = models.TextField()

    def __str__(self):
        return f"{self.product.product_name} - {self.score_percentage}%"
    
    class Meta:
        db_table = 'health_healthscore'


class Reward(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    points = models.IntegerField()
    activity = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.points}"
    class Meta:
        db_table = 'health_reward'


class ScanHistory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    scanned_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} scanned {self.product.product_name}"
    class Meta:
        db_table = 'health_scanhistory'


from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Product, Nutrition, HealthScore, Reward, ScanHistory
from .form import ScanForm


# 🧮 Health Score Calculation Logic
def calculate_health_score(nutrition):
    score = 100

    if nutrition.sugar > 20:
        score -= 20
    if nutrition.sodium > 500:
        score -= 20
    if nutrition.fat > 15:
        score -= 15
    if nutrition.fiber > 5:
        score += 10

    return max(0, min(score, 100))


# 🏠 Home Page
def home(request):
    return render(request, "health/home.html")


# 🔍 Scan Product View
@login_required
def scan_product(request):
    form = ScanForm()
    context = {"form": form}

    if request.method == "POST":
        form = ScanForm(request.POST)
        if form.is_valid():
            barcode = form.cleaned_data["barcode"]
            product = get_object_or_404(Product, barcode=barcode)
            nutrition = Nutrition.objects.get(product=product)

            # Calculate score dynamically
            score = calculate_health_score(nutrition)

            # Save scan history
            ScanHistory.objects.create(user=request.user, product=product)

            # Add reward points
            Reward.objects.create(user=request.user, points=10, activity="Product Scan")

            context = {
                "product": product,
                "nutrition": nutrition,
                "score": score
            }

            return render(request, "health/scan_result.html", context)

    return render(request, "health/scan.html", context)


# 🎁 Reward View
@login_required
def my_rewards(request):
    rewards = Reward.objects.filter(user=request.user)
    total_points = sum(r.points for r in rewards)

    return render(request, "health/rewards.html", {
        "rewards": rewards,
        "total_points": total_points
    })

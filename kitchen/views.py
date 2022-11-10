from django.contrib.auth import get_user_model
from django.shortcuts import render

from kitchen.models import Dish, DishType


def index(request):
    num_dishes = Dish.objects.count()
    num_cooks = get_user_model().objects.count()
    num_dish_types = DishType.objects.count()
    num_visits = request.session.get("visit_count", 1)
    request.session["visit_count"] = num_visits + 1

    context = {
        "num_dishes": num_dishes,
        "num_cooks": num_cooks,
        "num_dish_types": num_dish_types,
        "num_visits": num_visits,
    }

    return render(request, "kitchen/index.html", context)

from django.contrib.auth import get_user_model
from django.shortcuts import render

from kitchen.models import Dish


def index(request):
    num_dishes = Dish.objects.count()
    num_cooks = get_user_model().objects.count()

    context = {
        "num_dishes": num_dishes,
        "num_cooks": num_cooks
    }

    return render(request, "kitchen/index.html", context)

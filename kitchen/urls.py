from django.urls import path

from kitchen.views import (
    index,
    DishTypeListView,
    DishListView,
    CookListView,
    DishDetailView,
    CookDetailView,
    CookCreateView,
)

urlpatterns = [
    path("", index, name="index"),
    path("dish-types/f", DishTypeListView.as_view(), name="dish-type-list"),
    path("dishes/", DishListView.as_view(), name="dishes-list"),
    path("dishes/<int:pk>/", DishDetailView.as_view(), name="dishes-detail"),
    path("cooks/", CookListView.as_view(), name="cooks-list"),
    path("cooks/<int:pk>/", CookDetailView.as_view(), name="cooks-detail"),
    path("cooks/create/", CookCreateView.as_view(), name="cooks-create"),
]

app_name = "kitchen"

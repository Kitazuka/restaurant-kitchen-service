from django.urls import path

from kitchen.views import (
    index,
    DishTypeListView,
    DishListView,
    CookListView,
    DishDetailView,
    CookDetailView,
    CookCreateView,
    DishCreateView,
    DishUpdateView,
    # DishTypeCreateView,
)

urlpatterns = [
    path("", index, name="index"),
    path("dish-types/", DishTypeListView.as_view(), name="dish-type-list"),
    # path("dish-types/create", DishTypeCreateView.as_view(), name="dish-type-list"),
    path("dishes/", DishListView.as_view(), name="dishes-list"),
    path("dishes/<int:pk>/", DishDetailView.as_view(), name="dishes-detail"),
    path("dishes/create/", DishCreateView.as_view(), name="dishes-create"),
    path("dishes/<int:pk>/update", DishUpdateView.as_view(), name="dishes-update"),
    path("cooks/", CookListView.as_view(), name="cooks-list"),
    path("cooks/<int:pk>/", CookDetailView.as_view(), name="cooks-detail"),
    path("cooks/create/", CookCreateView.as_view(), name="cooks-create"),
]

app_name = "kitchen"

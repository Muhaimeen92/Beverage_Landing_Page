from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<str:order_number>", views.display_order, name="display_order")
]
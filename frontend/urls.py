from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("confirmation/<str:order_number>", views.confirmation, name="confirmation")

]
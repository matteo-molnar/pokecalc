from django.urls import path

from typecalculator import views


urlpatterns = [
    path("", views.index, name="index"),
]

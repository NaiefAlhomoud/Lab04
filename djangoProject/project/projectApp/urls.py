from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("/<int:number>", views.tax, name="tax"),
    path("/taxrate", views.taxrate, name="taxrate")
]
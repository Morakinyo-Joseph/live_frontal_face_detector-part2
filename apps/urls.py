from django.urls import path
from . import views

app_name = "apps"

urlpatterns = [
    # path("", views.starter, name="starter"),

    path("", views.capture_face, name="face"),
    ]

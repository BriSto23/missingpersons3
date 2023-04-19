# Missing Persons Group Project
# Garrett Ashcroft, Charlotte Griffin, Brian Stone, Andrew Hunsaker, Amy Dutson, Preston Vance

from django.urls import path
from .views import indexPageView, dataPageView, learnPageView

urlpatterns = [
    path("", indexPageView, name="index"),
    path("data", dataPageView, name="data"),
    path("learn/<str:id>/", learnPageView, name="learn"),
]

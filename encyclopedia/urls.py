from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<str:name>/", views.article, name="article"),
    # path("<str:name>/", views.test, name="test")
]

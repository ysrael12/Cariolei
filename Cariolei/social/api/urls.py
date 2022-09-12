from django.contrib import admin
from django.urls import path
from .views import TheModelView, TheModelViewTwo

urlpatterns = [

    path('themodel/', TheModelView),
    path('themodel/<int:id>/', TheModelViewTwo)
]


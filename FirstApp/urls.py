from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [
    path('add/<int:num1>/<int:num2>', views.add),
    path('minus/<int:num1>/<int:num2>', views.minus),
    path('div/<int:num1>/<int:num2>', views.div),
]
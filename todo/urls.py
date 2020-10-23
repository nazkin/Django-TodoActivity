from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="list"),
    path('manage_task/<str:pkey>/', views.manageTask, name="manage"),
    path('remove_task/<str:pkey>/', views.removeTask, name="remove")
]
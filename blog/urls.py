from django.urls import path
from . import views


urlpatterns = [
    path('list/', views.list, name="list"),
    path('form/', views.form, name="form"),
    path('update/', views.update, name="update")
]
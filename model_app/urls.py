from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.print_list, name="print_list"),
    # path('form/', views.create_form, name="create_form"),
    path('form/', views.form, name="form"),
    # path('confirm/', views.confirm, name="confirm")
]
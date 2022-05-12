from django.urls import path

from . import views


app_name = 'menuapp'

urlpatterns = [
    path('', views.get_menu, name='menu'),
]

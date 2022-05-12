from django.urls import path

from . import views

app_name = 'lottoapp'

urlpatterns = [
    path('', views.get_lotto_nums, name='lotto'),
]

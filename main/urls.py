from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('new_purchase', views.new_purchase, name='new_purchase')
]

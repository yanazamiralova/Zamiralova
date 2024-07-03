from django.urls import path
from django.conf import settings
from .views import create_statements,UserOrdersListView
from . import views

urlpatterns = [
    path('', views.index),
    path('about', views.about),
    path('create_statements', create_statements, name='create_statements'),
    path('statements', UserOrdersListView.as_view(), name='statement_list'),
]

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('Europe', views.europe_window, name='Europe'),
    path('Ukraine', views.ukraine_window, name='Ukraine'),
    path('Asia', views.asia_window, name='Asia'),
]
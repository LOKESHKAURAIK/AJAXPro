from django.urls import path
from . import views
urlpatterns = [
    path('', views.index),
    path('ajaxdata', views.ajaxdata)

]

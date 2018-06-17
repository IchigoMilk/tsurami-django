from django.urls import path
from . import views

app_name = 'tsurami'
urlpatterns = [
    path('', views.PostIndexView.as_view(), name='index'),
]

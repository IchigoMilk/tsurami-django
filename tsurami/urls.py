from django.urls import path
from . import views

app_name = 'tsurami'
urlpatterns = [
    # path('', views.IndexView.as_view(), name='index'),
    path('', views.MyListView.as_view(), name='index'),
]

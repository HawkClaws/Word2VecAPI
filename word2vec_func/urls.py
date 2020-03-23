from django.urls import path
from . import views

urlpatterns = [
    path('', views.word2vec_calc, name='word2vec'),
]
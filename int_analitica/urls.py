from django.urls import path
from .views import index_int_analitica

urlpatterns = [
    path('index/', index_int_analitica, name="index-int-analitica")
]
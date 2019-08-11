from django.urls import path
from .views import index_int_numerica, new_int_numerica

urlpatterns = [
    path('index/', index_int_numerica, name="index_int_numerica"),
    path('new/', new_int_numerica, name="new_int_numerica")
]
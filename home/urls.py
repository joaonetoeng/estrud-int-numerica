from django.urls import path
from .views import home, my_logout, admin, pilares

urlpatterns = [
    path('', home, name="home"),
    path('admin/', admin, name="admin"),
    path('pilares/', pilares, name="pilares"),
    path('logout/', my_logout, name="logout"),
]
from django.urls import path
from .views import index, memory_new, memory_update, memory_delete

urlpatterns = [
    path('index/', index, name="index"),
    path('new/', memory_new, name="memory_new"),
    path('update/<int:id>', memory_update, name="memory_update"),
    path('delete/<int:id>', memory_delete, name="memory_delete")
]
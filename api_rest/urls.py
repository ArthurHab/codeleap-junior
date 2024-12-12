from django.urls import path

from . import views

urlpatterns = [
    path('', views.list_and_create, name='list_and_create'),
    path('<int:id>', views.get_update_delete, name='get_update_delete'),
]

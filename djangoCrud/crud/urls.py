from django.urls import path
from . import views

urlpatterns = [
    path('',views.create,name="user_create"),
    path('update/<int:id>',views.update,name="user_update"),
    path('delete/<int:id>',views.delete,name="user_delete"),
    
]
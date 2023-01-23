from django.urls import path
from .views import home,todo


urlpatterns = [
    path('',home,name="home"),
    path('todo/<str:id>',todo,name="todo"),
]

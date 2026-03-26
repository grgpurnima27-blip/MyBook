from django.urls import path 
from .views import home, detail,add
urlpatterns = [
    path('',home),
    path('detail/<int:id>/',detail),
    path("create/",add),
]

from django.urls import path
from . import views

urlpatterns = [
    path("",views.ReviewView.as_view(),name="home"),
    path("success",views.success,name="success")
]

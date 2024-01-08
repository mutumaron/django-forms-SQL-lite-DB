from django.urls import path
from . import views

urlpatterns = [
    path("",views.ReviewView.as_view(),name="home"),
    path("success",views.Success.as_view(),name="success"),
    path("reviews",views.ReviewsListView.as_view()),
    path("reviews/favorite",views.AddFavoriteView.as_view()),
    path("reviews/<int:pk>",views.SingleReview.as_view())
]

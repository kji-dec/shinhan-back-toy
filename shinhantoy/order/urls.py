from django.urls import path
from . import views

urlpatterns = [
    path("", views.OrderListView.as_view()),
    path("/<int:pk>", views.OrderDetailView.as_view()),
    path("/<int:order_id>/comment", views.CommentListView.as_view()),
    path("/<int:order_id>/comment/<int:pk>", views.CommentDeleteView.as_view()),
    path("/<int:order_id>/comment/<int:comment_id>/like", views.LikeCreateView.as_view()),
]
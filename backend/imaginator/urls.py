from django.urls import path

from . import views

urlpatterns = [
    path("images/", views.DeepColorResultList.as_view(), name="image_list"),
    path(
        "images/<int:pk>/", views.DeepColorResultDetail.as_view(), name="image_detail"
    ),
    path("strategies/", views.strategies, name="strategies"),
]

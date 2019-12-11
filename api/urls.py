from django.urls import path

from api import views

urlpatterns = [
    path('user/',views.UserView.as_view(),name ="user-list"),
    path('user/<pk>/',views.UserDetail.as_view(),name="user-detail")
]
from django.urls import path

from . import views

urlpatterns = [
    path('user/', views.user_mixin_view),
    path('user/<int:pk>/', views.user_mixin_view)
]
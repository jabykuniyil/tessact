from django.urls import path
from . import views


urlpatterns = [
    path('', views.blog_mixin_view),
    path('<int:pk>/', views.blog_mixin_view),
    # path('blogs/', views.blog_mixin_view),
]

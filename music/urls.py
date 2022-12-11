from django.urls import path

from . import views

urlpatterns = [
    path('', views.index_page, name="index"),
    path('bookForm/', views.get_details, name="book"),
    path('aboutPage/', views.about_page, name="about"),
    # path('login', views.login, name='login'),
]
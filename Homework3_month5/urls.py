"""
URL configuration for Homework3_month5 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls import path
from otziv.views import (DirectorListCreateView, DirectorDetailView,
                    MovieListCreateView, MovieDetailView, ReviewListCreateView, ReviewDetailView)
urlpatterns = [
    # Director routes
    path('api/v1/directors/', DirectorListCreateView.as_view(), name='director-list-create'),
    path('api/v1/directors/<int:id>/', DirectorDetailView.as_view(), name='director-detail'),

    # Movie routes
    path('api/v1/movies/', MovieListCreateView.as_view(), name='movie-list-create'),
    path('api/v1/movies/<int:id>/', MovieDetailView.as_view(), name='movie-detail'),

    # Review routes
    path('api/v1/reviews/', ReviewListCreateView.as_view(), name='review-list-create'),
    path('api/v1/reviews/<int:id>/', ReviewDetailView.as_view(), name='review-detail'),
]
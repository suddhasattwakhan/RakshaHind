from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('crime/create/', views.create_crime, name='create_crime'),
    path('crime/bookmark/<int:crime_id>/', views.bookmark_crime, name='bookmark_crime'),
    path('', views.crime_listing, name='crime_listing'),
    path('bookmark/listing/', views.bookmark_listing, name='bookmark_listing'),
]

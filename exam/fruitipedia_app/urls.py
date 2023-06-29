from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('create/', views.create_fruit, name='create_fruit'),
    path('<int:pk>/', include([
        path('details/', views.fruit_details, name='fruit_details'),
        path('edit/', views.fruit_edit, name='fruit_edit'),
        path('delete/', views.fruit_delete, name='fruit_delete'),
    ])),
    path('profile/', include([
        path('create/', views.profile_create, name='profile_create'),
        path('details/', views.profile_details, name='profile_details'),
        path('edit/', views.profile_edit, name='profile_edit'),
        path('delete/', views.profile_delete, name='profile_delete'),
    ]))
]

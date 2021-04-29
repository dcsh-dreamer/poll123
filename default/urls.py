from django.urls import path
from . import views

urlpatterns = [
    path('poll2/', views.poll_list), 
    path('poll/', views.PollList.as_view()), 
    path('poll/<int:pk>/', views.PollDetail.as_view()), 
]
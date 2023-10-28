from django.urls import path
from labApp import views

# from . import views
urlpatterns = [
    path('courses/', views.courses, name='courses'),
    path('students/', views.students, name='students'),
    path('details/<int:studentId>/', views.details, name='details')
]
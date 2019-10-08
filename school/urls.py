from django.urls import path

from . import views

urlpatterns = [
    path('', views.SchoolView.as_view()),
    path('<int:pk>/', views.SchoolView.as_view()),
    path('<int:pk>/register/', views.StudentRegistrationView.as_view()),
    path('<int:pk>/students/', views.StudentsListView.as_view()),
]
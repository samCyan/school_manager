# api/urls.py
from django.urls import path, include

from . import views

urlpatterns = [
    path('schools/', include('school.urls')),
    path('students/', include('student.urls')),
    path('rest-auth/', include('rest_auth.urls')),
    path('rest-auth/registration/', include('rest_auth.registration.urls')),

]
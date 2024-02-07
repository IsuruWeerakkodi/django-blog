from django.urls import path, re_path
from blog.views import schools_view

urlpatterns = [
    path('schools/', schools_view, name='schools'),
    # Other URL patterns...
]

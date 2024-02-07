from django.shortcuts import render
from blog.models import School,ClassName

# Create your views here.
# views.py

def schools_view(request):
    schools = School.objects.all()
    return render(request, 'schools.html', {'schools': schools})

    class_name = ClassName.objects.all()
    return render(request, 'schools.html', {'class_name': class_name})


from django.shortcuts import render
from blog.models import School,ClassName

# Create your views here.
# views.py

def schools_view(request):
    schools = School.objects.all()
    return render(request, 'schools.html', {'schools': schools})

    class_name = ClassName.objects.all()
    return render(request, 'schools.html', {'class_name': class_name})

    assessment_areas = School.objects.all()
    return render(request, 'schools.html', {'assessment_areas': assessment_areas})

    full_name = School.objects.all()
    return render(request, 'schools.html', {'full_name': full_name})

    answers = School.objects.all()
    return render(request, 'schools.html', {'answers': answers})

    awards = School.objects.all()
    return render(request, 'schools.html', {'awards': awards})

    subject = School.objects.all()
    return render(request, 'schools.html', {'subject': subject})
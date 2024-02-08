from django.shortcuts import render
from blog.models import School, ClassName, AssessmentAreas, Student, Answers, Awards, Subject

def schools_view(request):
    schools = School.objects.all()
    class_names = ClassName.objects.all()
    assessment_areas = AssessmentAreas.objects.all()
    students = Student.objects.all()
    answers = Answers.objects.all()
    awards = Awards.objects.all()
    subjects = Subject.objects.all()

    return render(request, 'schools.html', {
        'schools': schools,
        'class_names': class_names,
        'assessment_areas': assessment_areas,
        'students': students,
        'answers': answers,
        'awards': awards,
        'subjects': subjects,
    })



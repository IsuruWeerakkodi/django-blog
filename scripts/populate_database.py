import os
import sys
import csv

# Add the path to your project to the Python path
sys.path.append('/home/isuru/Documents/django-application')
csv_file_path = '/home/isuru/Documents/django-application/data/data.csv'

# Set up the django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'personal_blog.settings')
import django
django.setup()

from blog.models import School,ClassName, AssessmentAreas, Student, Answers, Awards, Subject

def populate_database_from_csv(csv_file_path):
    with open(csv_file_path, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            School.objects.create(
                id = row['StudentID'],
                name=row['school_name'],
            )    

            ClassName.objects.create(
                id=row['StudentID'],
                class_name=row['Class'],
            )
            AssessmentAreas.objects.create(
                id=row['StudentID'],
                assessment_ares = row['Assessment Areas']
            )

            Student.objects.create(
                id=row['StudentID'],
                full_name = row['First Name'] + row['Last Name']
            )

            Answers.objects.create(
                id=row['StudentID'],
                answers = row['Answers']
            )

            Awards.objects.create(
                id=row['StudentID'],
                awards = row['award']
            )

            Subject.objects.create(
                id=row['StudentID'],
                subject = row['Subject'],
                subject_score = row['sydney average score']
            )

# if __name__ == "__main__":
#     csv_file_path = '/home/isuru/Documents/django-application/data/data.csv'
#     populate_database_from_csv(csv_file_path)

populate_database_from_csv('/home/isuru/Documents/django-application/data/data.csv')
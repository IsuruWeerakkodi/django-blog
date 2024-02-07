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

from blog.models import School,ClassName

def populate_database_from_csv(csv_file_path):
    with open(csv_file_path, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            School.objects.create(
                name=row['school_name'],
                # Add more fields as needed
            )    

            ClassName.objects.create(
                class_name=row['year'],
                # Add more fields as needed    
            )    

# if __name__ == "__main__":
#     csv_file_path = '/home/isuru/Documents/django-application/data/data.csv'
#     populate_database_from_csv(csv_file_path)

populate_database_from_csv('/home/isuru/Documents/django-application/data/data.csv')
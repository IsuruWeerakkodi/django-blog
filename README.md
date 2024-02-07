# Django App

## Introduction
Welcome to my Django application! This application is designed to provide data about the students, and their academic performances from the schools in Austrailia. It is built using the Django web framework, which allows for rapid development of web applications in Python.

## Prerequisites
- Python (3.6 or higher)
- Django framework

## Installation
1. Clone this repository to your local machine:

   ```
   git clone https://github.com/IsuruWeerakkodi/djangoapp.git
   ```

2. Navigate to the project directory:

   ```
   cd djangoapp
   ```

3. Install the required Python packages:

   ```
   pip install -r requirements.txt
   ```

## Database Setup
1. Make migrations for the database models:

   ```
   python manage.py makemigrations
   ```

2. Apply migrations to create the database tables:

   ```
   python manage.py migrate
   ```

## Running the App
1. Start the Django development server:

   ```
   python manage.py runserver
   ```

2. Access the app in your web browser at `http://127.0.0.1:8000/`.

## Usage
- Once the app is running, you can navigate to different URLs to interact with the app features.
- Use the Django admin interface (`http://127.0.0.1:8000/admin/`) to manage departments, employees, projects, skills, and managers.

## Testing
- Run the automated tests for the app:

  ```
  python manage.py test
  ```

## Docker Support
- This app can also be run using Docker for containerization.
- Build the Docker image:

  ```
  docker build -t django-app .
  ```

- Run the Docker container:

  ```
  docker run -p 8000:8000 django-app
  ```

## Contributing
- Contributions are welcome! Feel free to submit pull requests or raise issues.

## License
- This project is licensed under the [MIT License](LICENSE).

## Authors
- [Isuru Weerakkodi](https://github.com/IsuruWeerakkodi)

## Contact
If you have any questions or suggestions, feel free to reach out to the project maintainer: Email: isuruweerakkodi24@gmail.com

Copyright &copy; 2024 Isuru Weerakkodi. All Rights Reserved.


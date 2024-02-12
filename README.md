# FullstackDjango

Installation
Clone the repository to your local machine.

Create a virtual environment and activate it.

python -m venv venv

Install Django and Django REST Framework.
pip install django djangorestframework


Install the project dependencies.
pip install -r requirements.txt

Apply database migrations.
python manage.py makemigrations
python manage.py migrate


Create superusers.

python manage.py createsuperuser --email iit2020165@iiita.ac.in --username iit2020165
python manage.py createsuperuser --email vansh.narang12@gmail.com --username vansh.narang12
Both superusers have the password 1234.

Run the development server.

Copy code
python manage.py runserver
Usage
Access the admin panel at http://localhost:8000/admin/ to manage items, categories, and tags. Use the superuser credentials provided above.

Access the API endpoints at http://localhost:8000/items/ for CRUD operations on items.

Testing
To run tests, execute the following command:

bash
python manage.py test
Database Setup and Migration

Setup
By default, this project uses SQLite as the database. However, you can configure it to use other databases such as PostgreSQL, MySQL, etc., by updating the DATABASES setting in settings.py.

Migration
To create migrations for any changes to the models, run the following command:
python manage.py makemigrations
And then apply the migrations using:

python manage.py migrate

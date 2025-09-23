This project was made based on BU CS412 <br />
My Website: https://annaandmandy.pythonanywhere.com/

# create/start the django project in the current directory
pipenv shell
cd cs412

# run this command to start your django project called 412.
django-admin startproject cs412

# run the django development server
python manage.py runserver

# create the migrations: the updates to the database models
python manage.py makemigrations

# apply the migrations
python manage.py migrate

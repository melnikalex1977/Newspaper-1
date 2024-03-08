# Newspaper
Django project for managing newspaper

project develoyed to Render (https://newspaper-1.onrender.com/)

 
1 Read before start
1.1 Prepare the project
   -Fork the repo (GitHub repository)
   -Clone the forked repo
   git clone the-link-from-your-forked-repo
(You can get the link by clicking the Clone or download button in your repo)

   - Open the project folder in your IDE
   - Open a terminal in the project folder
   - Create a branch for the solution and switch on it
   git checkout -b develop
(You can use any other name instead of develop)

     - If you are using PyCharm - it may propose you to automatically create venv for 
your project and install requirements in it, but if not:
   python -m venv venv
   venv\Scripts\activate (on Windows)
   source venv/bin/activate (on macOS)
   pip install -r requirements.txt
   python manage.py runserver

2 This project implements search functionality for all 3 content pages:
   - redactor
   - newsapaper
   - topic
3. In this project, tests are written for the search function, for custom and for core project features. 
Tests are written using the following resources (https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Testing)

![Website Interface](demo.png)

to log into my system you must use:
   login: admin
   password: admin12345


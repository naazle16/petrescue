🐾 PetRescue – Milestone 1
📘 Project Overview

PetRescue is a Django-based web application that helps connect pet rescuers and adopters on a single platform.
The goal is to make it easier for users to report lost or found pets, browse available pets for adoption, and connect with pet shelters.

🚀 Milestone 1 Goals

✅ Setup Django project structure
✅ Create initial app (petusers)
✅ Configure templates and static files
✅ Create and test the Home Page and Login Page
✅ Verify that login page opens successfully in browser

🧱 Folder Structure
petrescue/
│
├── manage.py
├── petrescue/            # Main Django project folder
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
│
├── petusers/              # App containing user-related views and templates
│   ├── views.py
│   ├── models.py
│   ├── templates/
│   │   ├── base.html
│   │   ├── home.html
│   │   └── login.html
│
└── README.md

🖥️ Features in Milestone 1

Home Page: Welcoming layout introducing PetRescue

Login Page: Simple and functional user login design

Navigation: Easy transition between pages

Attractive UI: Styled using HTML and CSS templates

⚙️ Setup Instructions (for Mentor)

To run the project locally:

# Clone the repository
git clone https://github.com/naazle16/petrescue.git

# Move into the folder
cd petrescue

# Create and activate virtual environment (optional)
python -m venv venv
venv\Scripts\activate    # on Windows

# Install Django
pip install django

# Run the server
python manage.py runserver


Now open your browser and go to:
👉 http://127.0.0.1:8000/

🧩 Next Milestone (Milestone 2 Plan)

Add user registration and authentication

Create pet registration module

Build database models for pets and users

Improve UI design and add dashboard

👩‍💻 Developer

Name: Patan Naazle Firdos
Course: B.Tech – CSE (Final Year)
College: Ravindra College of Engineering for Women, Kurnool
# 🐾 PetRescue – Milestone 1  

## 📘 Project Overview  
**PetRescue** is a Django-based web application that helps connect pet rescuers and adopters on a single platform.  
The goal is to make it easier for users to:  
- Report lost or found pets  
- Browse available pets for adoption  
- Connect with pet shelters  

---

## 🚀 Milestone 1 Goals  
✅ Setup Django project structure  
✅ Create initial app (`petusers`)  
✅ Configure templates and static files  
✅ Create and test the **Home Page** and **Login Page**  
✅ Verify that login page opens successfully in the browser  

---

## 🧱 Folder Structure  
petrescue/
│
├── manage.py
│
├── petrescue/ # Main Django project folder
│ ├── settings.py
│ ├── urls.py
│ ├── wsgi.py
│ └── asgi.py
│
├── petusers/ # App containing user-related views and templates
│ ├── views.py
│ ├── models.py
│ ├── templates/
│ │ ├── base.html
│ │ ├── home.html
│ │ └── login.html
│
└── README.md

---

## 🖥️ Features Implemented in Milestone 1  
- **Home Page:** Welcoming layout introducing PetRescue  
- **Login Page:** Simple and functional user login design  
- **Navigation:** Easy transition between pages  
- **Attractive UI:** Styled using HTML and CSS templates  

---

## ⚙️ Setup Instructions (for Mentor)  

    To run the project locally:  

1. **Clone the repository**  
    git clone https://github.com/naazle16/petrescue.git
2. **Move into the project folder**

    cd petrescue


3. **(Optional) Create and activate virtual environment**

    python -m venv venv
    venv\Scripts\activate   # on Windows


4. **Install Django**

    pip install django


5. **Run the server**

    python manage.py runserver


6. **Open in browser**
    👉 http://127.0.0.1:8000/

# Django Task Manager

A simple and user-friendly Task Management Web Application built using Python and Django.

## Project Overview

Django Task Manager helps users organize their daily tasks, track progress, set deadlines, and manage priorities.

Each registered user can create and manage their own tasks securely.

## Features

- User Registration and Login
- Secure User Authentication
- Add New Tasks
- Edit Existing Tasks
- Delete Tasks
- Mark Tasks as Completed
- Set Task Due Dates
- Set Task Priorities (Low, Medium, High)
- Search Tasks by Title
- Filter Tasks by Priority
- Dashboard Statistics
- User-specific Task Management

## Technologies Used

- Python
- Django
- HTML
- CSS
- SQLite
- Git
- GitHub

## Project Structure

```text
django_task_manager/
│
├── accounts/
│   ├── migrations/
│   ├── urls.py
│   └── views.py
│
├── config/
│   ├── settings.py
│   └── urls.py
│
├── tasks/
│   ├── migrations/
│   ├── static/
│   ├── templates/
│   ├── models.py
│   ├── views.py
│   └── urls.py
│
├── templates/
│   └── accounts/
│
├── manage.py
└── README.md
```

## Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/iswza123/django-task-manager.git
```

### 2. Navigate to the project folder

```bash
cd django-task-manager
```

### 3. Create a virtual environment

```bash
python3 -m venv venv
```

### 4. Activate the virtual environment

```bash
source venv/bin/activate
```

### 5. Install Django

```bash
pip install Django
```

### 6. Set the Django secret key

```bash
export DJANGO_SECRET_KEY="your-secret-key"
```

Generate your own secret key locally. Never share or upload it.

### 7. Apply database migrations

```bash
python3 manage.py migrate
```

### 8. Run the development server

```bash
python3 manage.py runserver
```

Open your browser and visit:

http://127.0.0.1:8000/

## Learning Outcomes

Through this project, I gained practical experience in:

- Django application development
- Python programming
- CRUD operations
- Database models and migrations
- User authentication
- Django views, URLs, and templates
- HTML and CSS integration
- Git and GitHub version control

## Author

**Fathima Wafa**

GitHub: https://github.com/iswza123

---

*This project was developed as a hands-on learning project to improve my Python and Django web development skills.*
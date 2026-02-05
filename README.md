# Task Manager

Task Manager is a web application built with **Django** and **Django Rest Framework** for managing project tasks. Users can view, search, create, update, and delete tasks. Each task has a **title**, **description**, **status**, and **owner**, and users can only modify their own tasks.

## Features

- **User Authentication:** login/logout for predefined users (no registration required)  
- **Task Management:** CRUD operations with ownership restrictions  
- **Search & Details:** search tasks by title/description, view full details  

## API Endpoints

- `GET /api/tasks/` → list tasks  
- `POST /api/tasks/` → create task  
- `GET/PUT/DELETE /api/tasks/<id>/` → task detail, update, delete  

## Database

- **Models:** Task linked to Django User  
- **ER Diagram:** included in `/docs/er_diagram.png`  

## Bonus

- Basic **test system** for key views (run with `python manage.py test`)  

## Setup

1. Install dependencies:  
    pip install -r requirements.txt

2. Apply migrations:
    python manage.py migrate

3. Create a superuser:
    python manage.py createsuperuser

4. Run server:
    python manage.py runserver

5. Open http://127.0.0.1:8000/tasks/ in your browser

   

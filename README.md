# Django Book CRUD App 

## Overview
This is a **Django web application** to manage books. It provides full **CRUD functionality** (Create, Read, Update, Delete) using Django models, views, forms, and templates.  
This project is ideal for learning Django basics and how to build a functional web app.

---

## Features
- **Home Page:** Displays a list of all books.
- **Detail Page:** Shows complete information about a single book.
- **Create Book:** Add new books to the database.
- **Edit Book:** Update existing book details.
- **Delete Book:** Remove a book with a confirmation prompt.
- **Dynamic URLs:** Uses Django URL names for navigation.
- **Safe object fetching:** `get_object_or_404` prevents errors for invalid IDs.
- **Bootstrap styling:** All templates use responsive design for better UI.

---

## Project Structure
```
BOOKPURCHASE/          <-- Root project folder
│
├── aboutbook/          <-- Django app
│   ├── __pycache__/
│   ├── migrations/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
│
├── books/              <-- Main Django project folder
│   ├── __pycache__/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── env/                <-- Virtual environment
│   ├── Include/
│   ├── Lib/
│   └── Scripts/
│
├── templates/
│   └── aboutbook/      <-- Templates for aboutbook app
│       ├── create.html
│       ├── delete.html
│       ├── detail.html
│       ├── edit.html
│       ├── home.html
│       └── base.html
│
├── db.sqlite3          <-- SQLite database
├── manage.py
└── README.md

```
---
## Models
#### Book Model
```python
from django.db import models
# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=200)
    author= models.CharField(max_length=25)
    description= models.TextField()
    price= models.IntegerField()

    def __str__(self):
        return self.title
    
```
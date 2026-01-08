# Product Management Web Application

## Overview
This project is a Product Management web application built using Django.
It supports user authentication and role-based access control.

There are two roles in the system:
- Admin: Full CRUD access to products
- User: Read-only access to products

---

## Features
- User Registration & Login
- Role-based Authorization
- Product CRUD (Admin only)
- Product Listing & Product Details page
- Secure Logout
- Clean and functional UI

---

## Tech Stack
- Backend: Django
- Frontend: HTML, CSS
- Database: SQLite

---

## Project Structure

accounts/  
- Handles user registration, login, logout, and roles  

products/  
- Handles product CRUD operations  

templates/  
- HTML templates for UI  

---

## How to Run the Project

### Step 1: Clone Repository
```bash
git clone <repository_url>
cd product_management
```

### Step 2: Create Virtual Environment
```bash
python -m venv venv
venv\Scripts\activate
```

### Step 3: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 4: Run Migrations
```bash
python manage.py migrate
```

### Step 5: Create Superuser
```bash
python manage.py createsuperuser
```

### Step 6: Start Server
```bash
python manage.py runserver
```

## Open the Application
After starting the development server, open the application in your browser:

http://127.0.0.1:8000/

---

### Authorization Rules
- **Admin users** can add, edit, and delete products (full CRUD access).
- **Normal users** have read-only access and can only view product information.
- All authorization and permission checks are enforced at the **backend level**.

---

### Assumptions
- SQLite is sufficient for the scope of this assignment.
- The user interface is intentionally kept minimal and clean as per requirements.
- Django’s built-in authentication system is used to ensure secure user management.

---

### Notes
This project was developed as part of an assessment task.  
The primary focus areas include:
- Authentication and authorization
- Clean and maintainable project structure
- Correct implementation of CRUD operations









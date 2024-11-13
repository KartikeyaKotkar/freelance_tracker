# Freelance Tracker

## Description

The **Freelance Tracker** is a Django-based web application designed to help freelancers manage clients, projects, and invoices. The app allows users to track their work, deadlines, and payments, helping freelancers stay organized and manage their business more effectively.

This project provides a simple API for managing clients, projects, and invoices, with features for generating reports, tracking earnings, and exporting invoices.

---

## Features

- **Client Management**: Create, read, update, and delete client details.
- **Project Management**: Manage projects with details like status, deadline, and associated clients.
- **Invoice Management**: Create and manage invoices, track paid and overdue invoices.
- **Search**: View all active projects and overdue invoices.
- **Summary**: Calculate total monthly earnings and track completed projects.
- **Authentication**: Protect sensitive data with user authentication.
- **Export Feature**: Optional feature to export invoice details for bookkeeping.

---

## Folder Structure

The project has a modular structure, divided into apps for **clients**, **projects**, and **invoices**, along with a shared templates folder for the HTML views.

```
freelance_tracker/
├── freelance_tracker/          # Main project folder
│   ├── __init__.py
│   ├── settings.py             # Django settings
│   ├── urls.py                 # Main URL routing
│   ├── asgi.py                 # ASGI entry point
│   ├── wsgi.py                 # WSGI entry point
│   ├── manage.py               # Django management utility
├── clients/                    # App for managing clients
│   ├── __init__.py
│   ├── models.py               # Client data models
│   ├── views.py                # Views for managing clients
│   ├── urls.py                 # URL routing for client-related views
│   ├── forms.py                # Forms for adding and editing clients
│   ├── admin.py                # Django admin configuration for clients
│   ├── migrations/             # Database migrations for client models
├── projects/                   # App for managing projects
│   ├── __init__.py
│   ├── models.py               # Project data models
│   ├── views.py                # Views for managing projects
│   ├── urls.py                 # URL routing for project-related views
│   ├── forms.py                # Forms for adding and editing projects
│   ├── admin.py                # Django admin configuration for projects
│   ├── migrations/             # Database migrations for project models
├── invoices/                   # App for managing invoices
│   ├── __init__.py
│   ├── models.py               # Invoice data models
│   ├── views.py                # Views for managing invoices
│   ├── urls.py                 # URL routing for invoice-related views
│   ├── forms.py                # Forms for adding and editing invoices
│   ├── admin.py                # Django admin configuration for invoices
│   ├── migrations/             # Database migrations for invoice models
├── db.sqlite3                  # SQLite database for storing data
└── templates/                  # Shared templates folder for all apps
    └── base.html               # Base template for all pages
```

---

## Installation

To get started with the Freelance Tracker project, follow these steps:

### 1. Clone the Repository

Clone the repository to your local machine.

```bash
git clone https://github.com/yourusername/freelance_tracker.git
```

### 2. Install Dependencies

Navigate to the project folder and install the required dependencies:

```bash
cd freelance_tracker
pip install -r requirements.txt
```

> Note: Make sure you have `virtualenv` set up and activated to avoid any version conflicts.

### 3. Set Up the Database

Run migrations to set up the database schema:

```bash
python manage.py migrate
```

### 4. Create a Superuser

To access the Django admin panel, create a superuser:

```bash
python manage.py createsuperuser
```

Follow the prompts to create an admin user.

### 5. Start the Development Server

Run the Django development server:

```bash
python manage.py runserver
```

Now you can access the app at `http://127.0.0.1:8000/`.

---

## Usage

### Accessing the Admin Panel

- Go to `http://127.0.0.1:8000/admin/` to log in to the Django admin panel using the superuser credentials you created.
- Here you can manage clients, projects, and invoices.

### Client, Project, and Invoice Management

You can create, update, and delete clients, projects, and invoices via the Django admin interface. The system tracks:

- **Client information**: Name, contact details, etc.
- **Project details**: Status, associated client, deadline, and more.
- **Invoice details**: Amount, paid status, due date, and more.

### Search and Summary

- **Search**: You can search for active projects or overdue invoices directly from the admin panel.
- **Summary**: View the total earnings for the current month and see how many projects have been completed.

---

## API Endpoints (Optional)

You can also interact with the data via the API if needed. For example:

- **Clients API**: `/api/clients/`
- **Projects API**: `/api/projects/`
- **Invoices API**: `/api/invoices/`
  
You can add API views using Django REST framework (if desired) to expose these endpoints for external usage.

---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## Contributing

Contributions are welcome! Feel free to fork this repository, submit issues, and send pull requests. If you have suggestions for improvement or want to report a bug, please open an issue.

---

## Future Improvements

- Add a **PDF export** feature for invoices.
- Implement **email notifications** for overdue invoices.
- Add **filters** and **sorting** for project and invoice management.
- Implement **client-side authentication** for additional security.

---

Feel free to modify or extend the project as needed.
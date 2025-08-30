# Django Timetable Management System

A simple, web-based timetable management system built with Django for the Faculty of Technology. This application allows administrators to create and manage class schedules, while students and teachers can view their respective timetables.

## Features

* **Admin Dashboard:** A powerful admin panel to manage subjects, teachers, classrooms, student groups, and timetable entries.
* **Dynamic Timetable View:** Displays a clean, grid-based timetable for any given student group.
* **Scalable Structure:** Built with a clear and scalable Django app structure, making it easy to add new features.

## Tech Stack

* **Backend:** Python, Django
* **Database:** SQLite3 (for development)
* **Frontend:** HTML, CSS

## Getting Started

Follow these instructions to get a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

You need to have Python and Pip installed on your system.

### Installation & Setup

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/YOUR_USERNAME/django-timetable-system.git](https://github.com/YOUR_USERNAME/django-timetable-system.git)
    cd django-timetable-system
    ```

2.  **Create and activate a virtual environment:**
    * On Windows:
        ```bash
        python -m venv .venv
        .\.venv\Scripts\activate
        ```
    * On macOS/Linux:
        ```bash
        python3 -m venv .venv
        source .venv/bin/activate
        ```

3.  **Install the dependencies:**
    ```bash
    pip install django
    ```

4.  **Apply database migrations:**
    This will create the necessary database tables.
    ```bash
    python manage.py migrate
    ```

5.  **Create a superuser account:**
    This account is needed to access the admin panel.
    ```bash
    python manage.py createsuperuser
    ```
    Follow the prompts to set up your username and password.

6.  **Run the development server:**
    ```bash
    python manage.py runserver
    ```
    The application will be running at `http://127.0.0.1:8000/`.

## Usage

1.  **Access the Admin Panel:**
    Navigate to `http://127.0.0.1:8000/admin/` and log in with the superuser credentials you created.

2.  **Add Data:**
    Before you can view a timetable, you must add some sample data through the admin panel:
    * Add at least one `Student Group` (e.g., "Computer Science - Year 3").
    * Add several `Subjects`, `Teachers`, and `Classrooms`.
    * Create `Timetable Entries` to build a schedule for the student group.

3.  **View the Timetable:**
    Once data is added, you can view the timetable for the first student group by visiting:
    ```
    [http://127.0.0.1:8000/timetables/group/1/](http://127.0.0.1:8000/timetables/group/1/)
    ```
    *(Replace `1` with the ID of the student group you wish to view.)*

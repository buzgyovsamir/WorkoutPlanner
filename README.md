# Workout Planner

A simple Django workout planner project for managing programs, workouts, and exercises.

## Project Summary

This project is built for a university assignment and demonstrates:

- 3 Django apps
- 3 related models
- validated forms
- class-based CRUD views
- shared templates with Bootstrap 5
- filtering and sorting pages
- custom template tags and filters
- custom 404 page

Authentication is intentionally not implemented because it is excluded by the assignment.

## Technologies Used

- Python 3.12
- Django 6
- PostgreSQL
- Bootstrap 5

## Apps Overview

- `programs`: program management
- `workouts`: workout management and assignment to programs
- `exercises`: exercise management and assignment to workouts

## Database Overview

Main relationships:

- `Workout -> Program`: many-to-one
- `Workout <-> Exercise`: many-to-many

The default configuration supports PostgreSQL.

For easier local testing, the project can also use SQLite when `USE_SQLITE=True`.

## Implemented Features

- Home page
- Program list, detail, create, update, delete
- Workout list, detail, create, update, delete
- Exercise list, detail, create, update, delete
- Assign exercises to a workout
- Filtered and sorted object pages
- Model and form validation
- Delete confirmation pages
- Shared base template, navbar, footer, and messages
- Custom template filter and inclusion tag
- Custom 404 page

## Setup Instructions

1. Clone the repository.
2. Open a terminal in the project folder.
3. Create a virtual environment.
4. Install dependencies.
5. Check the database configuration in `workoutPlanner/settings.py`.
6. Run migrations.
7. Start the development server.

## Virtual Environment

Windows PowerShell:

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

## Dependency Installation

```powershell
pip install -r requirements.txt
```

## PostgreSQL Configuration

1. Install PostgreSQL locally.
2. Create a database named `workout_planner_db` or set your own `DB_NAME`.
3. Update `DB_USER`, `DB_PASSWORD`, `DB_HOST`, and `DB_PORT` as needed.
4. Make sure the PostgreSQL server is running.

The project uses PostgreSQL in the default configuration.

## Optional SQLite Mode

For quick local testing only:

```env
USE_SQLITE=True
```

This helps the project run even if PostgreSQL is not ready yet.

## Migrations

```powershell
python manage.py makemigrations
python manage.py migrate
```

## Run the Server

```powershell
python manage.py runserver
```

Open:

- `http://127.0.0.1:8000/`

## Public Repository Readiness

This project is ready to be pushed to GitHub or another public repository.

Before publishing:

- do not commit real database passwords
- keep `USE_SQLITE=False` if you want to present the PostgreSQL version

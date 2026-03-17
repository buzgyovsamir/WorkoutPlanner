# Workout Planner

This is a small Django project for organizing workout programs, workouts, and exercises.

The idea is simple:
- a `Program` contains multiple `Workout` entries
- a `Workout` belongs to one `Program`
- a `Workout` can have multiple `Exercise` entries

The project was made as a university assignment, so the focus is on clear structure, CRUD functionality, form validation, and template work with Django.

## Tech stack

- Python 3.12
- Django 6
- PostgreSQL
- Bootstrap 5

## Apps

- `programs` - program data and program CRUD
- `workouts` - workout data, workout CRUD, and exercise assignment
- `exercises` - exercise data and exercise management

## Main features

- home page
- full CRUD for programs
- full CRUD for workouts
- exercise list, details, create, edit, and delete
- assigning exercises to workouts
- form validation in forms and models
- filtered and sorted list pages
- custom 404 page
- shared base template with navbar, footer, and messages

## Database

The default database is PostgreSQL.

Relationships used in the project:
- `Workout -> Program` is many-to-one
- `Workout <-> Exercise` is many-to-many

There is also an optional SQLite fallback in `settings.py` if you only want to test the project quickly without PostgreSQL.

## How to run the project

1. Clone the repository
2. Open the project folder
3. Create and activate a virtual environment
4. Install the dependencies
5. Check the database settings in [settings.py](d:\Coding - Samir\workoutPlanner\workoutPlanner\settings.py)
6. Run the migrations
7. Start the development server

## Virtual environment

Windows PowerShell:

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

## Install dependencies

```powershell
pip install -r requirements.txt
```

## PostgreSQL setup

Make sure PostgreSQL is installed and running locally.

By default, the project expects a database like this:
- database name: `workout_planner_db`
- host: `localhost`
- port: `5432`

If your PostgreSQL setup is different, update the database configuration in [settings.py](d:\Coding - Samir\workoutPlanner\workoutPlanner\settings.py).

## Migrations

```powershell
python manage.py makemigrations
python manage.py migrate
```

## Run the server

```powershell
python manage.py runserver
```

Then open:

`http://127.0.0.1:8000/`

## Notes

- Authentication is not included, because it is outside the assignment scope.
- The project uses Bootstrap for the layout and styling.
- The code is split into 3 apps so the responsibilities stay clear.

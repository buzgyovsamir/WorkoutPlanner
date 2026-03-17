from django.db import migrations


def fix_workout_exercises_m2m(apps, schema_editor):
    connection = schema_editor.connection
    existing_tables = set(connection.introspection.table_names())

    Workout = apps.get_model("workouts", "Workout")
    through_model = Workout._meta.get_field("exercises").remote_field.through
    through_table = through_model._meta.db_table
    legacy_table = "workouts_workoutexercise"

    if through_table not in existing_tables:
        schema_editor.create_model(through_model)

    if legacy_table not in existing_tables:
        return

    with connection.cursor() as cursor:
        cursor.execute(
            f"SELECT DISTINCT workout_id, exercise_id FROM {legacy_table}"
        )
        rows = cursor.fetchall()

    through_model.objects.using(connection.alias).bulk_create(
        [
            through_model(workout_id=workout_id, exercise_id=exercise_id)
            for workout_id, exercise_id in rows
        ],
        ignore_conflicts=True,
    )


class Migration(migrations.Migration):
    dependencies = [
        ("workouts", "0001_initial"),
    ]

    operations = [
        migrations.RunPython(
            fix_workout_exercises_m2m,
            migrations.RunPython.noop,
        ),
    ]

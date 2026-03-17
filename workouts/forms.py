from django import forms

from workouts.models import Workout


class WorkoutForm(forms.ModelForm):
    class Meta:
        model = Workout
        fields = ("title", "duration_minutes", "notes", "program")
        labels = {
            "title": "Workout name",
            "duration_minutes": "Duration (minutes)",
            "notes": "Notes",
            "program": "Program",
        }
        help_texts = {
            "title": "Use at least 3 characters.",
            "duration_minutes": "Enter the estimated workout duration.",
            "notes": "Optional notes for this workout.",
            "program": "Choose which program this workout belongs to.",
        }
        error_messages = {
            "title": {
                "required": "Please enter a workout name.",
            },
            "duration_minutes": {
                "required": "Please enter the workout duration.",
            },
            "program": {
                "required": "Please select a program.",
            },
        }
        widgets = {
            "title": forms.TextInput(
                attrs={"placeholder": "Example: Upper Body Day"}
            ),
            "duration_minutes": forms.NumberInput(
                attrs={"placeholder": "Example: 45", "min": 1}
            ),
            "notes": forms.Textarea(
                attrs={
                    "placeholder": "Optional notes about the workout...",
                    "rows": 4,
                }
            ),
            "program": forms.Select(),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            if isinstance(field.widget, forms.Select):
                field.widget.attrs["class"] = "form-select"
            else:
                field.widget.attrs["class"] = "form-control"

    def clean_title(self):
        title = self.cleaned_data["title"].strip()
        if len(title) < 3:
            raise forms.ValidationError(
                "Workout name must be at least 3 characters long."
            )
        return title

    def clean_duration_minutes(self):
        duration = self.cleaned_data["duration_minutes"]
        if duration < 1:
            raise forms.ValidationError("Duration must be at least 1 minute.")
        return duration


class WorkoutAssignExercisesForm(forms.ModelForm):
    class Meta:
        model = Workout
        fields = ("exercises",)
        labels = {
            "exercises": "Exercises",
        }
        help_texts = {
            "exercises": "Select one or more exercises for this workout.",
        }
        error_messages = {
            "exercises": {
                "required": "Please select at least one exercise.",
            },
        }
        widgets = {
            "exercises": forms.CheckboxSelectMultiple(),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["exercises"].widget.attrs["class"] = "form-check-input"

    def clean_exercises(self):
        exercises = self.cleaned_data["exercises"]
        if not exercises:
            raise forms.ValidationError(
                "Please choose at least one exercise for the workout."
            )
        return exercises

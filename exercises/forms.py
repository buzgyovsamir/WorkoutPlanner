from django import forms

from exercises.models import Exercise


class ExerciseForm(forms.ModelForm):
    class Meta:
        model = Exercise
        fields = (
            "name",
            "exercise_type",
            "description",
            "suggested_min_reps",
            "suggested_max_reps",
        )
        labels = {
            "name": "Exercise name",
            "exercise_type": "Exercise type",
            "description": "Description",
            "suggested_min_reps": "Suggested minimum reps",
            "suggested_max_reps": "Suggested maximum reps",
        }
        help_texts = {
            "name": "Use at least 3 characters.",
            "exercise_type": "Choose the exercise category.",
            "description": "Optional short explanation or cue.",
            "suggested_min_reps": "Optional lower rep recommendation.",
            "suggested_max_reps": "Optional upper rep recommendation.",
        }
        error_messages = {
            "name": {
                "required": "Please enter an exercise name.",
            },
            "exercise_type": {
                "required": "Please choose an exercise type.",
            },
        }
        widgets = {
            "name": forms.TextInput(
                attrs={"placeholder": "Example: Bench Press"}
            ),
            "description": forms.Textarea(
                attrs={
                    "placeholder": "Optional notes about the exercise...",
                    "rows": 4,
                }
            ),
            "suggested_min_reps": forms.NumberInput(
                attrs={"placeholder": "Example: 6", "min": 1}
            ),
            "suggested_max_reps": forms.NumberInput(
                attrs={"placeholder": "Example: 12", "min": 1}
            ),
        }

    def clean_name(self):
        name = self.cleaned_data["name"].strip()
        if len(name) < 3:
            raise forms.ValidationError(
                "Exercise name must be at least 3 characters long."
            )
        return name

    def clean(self):
        cleaned_data = super().clean()
        min_reps = cleaned_data.get("suggested_min_reps")
        max_reps = cleaned_data.get("suggested_max_reps")

        if min_reps and max_reps and min_reps > max_reps:
            self.add_error(
                "suggested_max_reps",
                "Maximum reps must be greater than or equal to minimum reps.",
            )

        return cleaned_data

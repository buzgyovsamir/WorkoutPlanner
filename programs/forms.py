from django import forms

from programs.models import Program


class ProgramForm(forms.ModelForm):
    form_note = forms.CharField(
        required=False,
        disabled=True,
        label="Note",
        initial="You can update the program details later.",
    )

    class Meta:
        model = Program
        fields = ("name", "goal", "level", "description")
        labels = {
            "name": "Program name",
            "goal": "Goal",
            "level": "Level",
            "description": "Description",
        }
        help_texts = {
            "name": "Use at least 3 characters.",
            "goal": "Choose the main goal of this program.",
            "level": "Select the training level.",
            "description": "Optional short summary for the program.",
        }
        error_messages = {
            "name": {
                "required": "Please enter a program name.",
            },
            "goal": {
                "required": "Please choose a goal.",
            },
            "level": {
                "required": "Please choose a level.",
            },
        }
        widgets = {
            "name": forms.TextInput(
                attrs={"placeholder": "Example: Full Body Starter"}
            ),
            "goal": forms.Select(),
            "level": forms.Select(),
            "description": forms.Textarea(
                attrs={
                    "placeholder": "Optional notes about the program...",
                    "rows": 4,
                }
            ),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name, field in self.fields.items():
            if isinstance(field.widget, forms.Select):
                css_class = "form-select"
            else:
                css_class = "form-control"
            field.widget.attrs["class"] = css_class

            if field.disabled:
                field.widget.attrs["readonly"] = True

    def clean_name(self):
        name = self.cleaned_data["name"].strip()
        if len(name) < 3:
            raise forms.ValidationError(
                "Program name must be at least 3 characters long."
            )
        return name

from django import forms
from question.models import Question
import re

type_choices = (
    ('General', 'General'),
    ('Advance', 'Advance'),
    ('Professional', 'Professional'),
)

class QuestionForm(forms.ModelForm):
    type = forms.ChoiceField(choices = type_choices, required = True)

    class Meta:
        model = Question
        fields = ['title', 'description', 'date', 'type']
        widgets = {
            'date': forms.DateInput(attrs={'placeholder': 'D/M/YYYY'})
        }

    def clean_title(self):
        title = self.cleaned_data.get("title")
        # title_list = title.split(' ')
        if len(title) <= 2:
            raise forms.ValidationError("Length can't be less than 3 letters.")

        else:
            return title

    def clean_description(self):
        description = self.cleaned_data.get("description")
        if not re.match("^[a-zA-Z0-9. ]+$", description):
            raise forms.ValidationError(("Remove invalid syntax from description."))
            # raise forms.ValidationError("Make sure the description is more than 3 letters")

        elif len(description) <= 2:
            raise forms.ValidationError("Short Description. Must have more than 3 letters.")

        else:
            return description

    def clean_date(self):
        # print("gjhj")
        date = self.cleaned_data.get("date")
        if not re.match("[0-9]{1,2}\/[0-9]{1,2}\/[0-9]{4}", date):
            raise forms.ValidationError("Invalid date format. Use DD/MM/YYYY format only!")
        else:
            return date

    def clean_type(self):
        type = self.cleaned_data.get("type")
        if not "General" and "Advance" and "Professional" in type:
            raise forms.ValidationError("No choice defined")
        else:
            return type


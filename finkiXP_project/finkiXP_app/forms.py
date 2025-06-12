from django import forms

from finkiXP_app.models import ExamTask


class TaskForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(TaskForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = ExamTask
        fields = ['subject', 'year', 'title', 'description', ]
        widgets = {
            'year': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
        }

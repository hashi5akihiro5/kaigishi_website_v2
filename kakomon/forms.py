from .models import Exam, Subject, Question
from django.forms import ModelForm, DateInput


class DateInput(DateInput):
    input_type = 'date'


class ExamForm(ModelForm):
    class Meta:
        model = Exam
        fields = [
            'exam_id',
            'date',
            'exam_type',
            'grade',
            'navigation_or_mechanism',
        ]
        widgets = {
            'date': DateInput()
        }

        def save(self, commit=True):
            exam = super().save(commit=False)
            if commit:
                exam.save()
            return exam

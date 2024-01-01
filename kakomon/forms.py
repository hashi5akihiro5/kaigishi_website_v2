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


class SubjectForm(ModelForm):
    class Meta:
        model = Subject
        fields = [
            'exam',
            'name',
            'name_order',
            'file_path',
        ]

        def save(self, commit=True):
            subject = super().save(commit=False)
            if commit:
                subject.save()
            return subject


class QuestionForm(ModelForm):
    class Meta:
        model = Question
        fields = [
            'subject',
            'question_id',
            'daimon',
            'shomon',
            'edamon',
            'similar_questions',
            'question_description',
            'question_image',
            'question',
            'answer_no_indent',
            'answer_image',
            'answer',
        ]

        def save(self, commit=True):
            question = super().save(commit=False)
            if commit:
                question.save()
            return question

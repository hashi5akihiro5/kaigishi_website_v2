from django.views.generic import ListView, TemplateView

from .constants import EXAMTYPE, GRADE, NAVIGATION_OR_ENGINEERING, SUBJECT
from .functions import find_key_for_value, get_exam_id
from .models import Exam, Question, Subject

""" Top画面 """


class IndexView(TemplateView):
    template_name = "kakomon/index.html"


""" 定期試験画面 """


class ExamListView(ListView):
    template_name = "kakomon/list_exam.html"
    model = Exam
    context_object_name = "exams"

    def get_form_kwargs(self):
        self.exam_type = find_key_for_value(self.kwargs.get("exam_type"), EXAMTYPE)
        self.navigation_or_engineering = find_key_for_value(
            self.kwargs.get("navigation_or_engineering"), NAVIGATION_OR_ENGINEERING
        )
        self.grade = find_key_for_value(self.kwargs.get("grade"), GRADE)

    def get_queryset(self):
        queryset = super().get_queryset()

        self.get_form_kwargs()

        # フィルタリング
        queryset = queryset.filter(
            exam_type=self.exam_type,
            navigation_or_engineering=self.navigation_or_engineering,
            grade=self.grade,
        )

        # 日付が新しい順で表示
        queryset = queryset.order_by("-date")
        return queryset

    def get_context_data(self):
        context = super().get_context_data()
        context.update(
            {
                "exam_type": self.kwargs.get("exam_type"),
                "navigation_or_engineering": self.kwargs.get(
                    "navigation_or_engineering"
                ),
                "grade": self.kwargs.get("grade"),
            }
        )
        return context


""" 科目画面 """


class SubjectListView(ListView):
    template_name = "kakomon/list_subject.html"
    model = Subject
    context_object_name = "subjects"

    def get_form_kwargs(self):
        self.exam_type = find_key_for_value(self.kwargs.get("exam_type"), EXAMTYPE)
        self.navigation_or_engineering = find_key_for_value(
            self.kwargs.get("navigation_or_engineering"), NAVIGATION_OR_ENGINEERING
        )
        self.grade = find_key_for_value(self.kwargs.get("grade"), GRADE)
        self.year = self.kwargs.get("year")
        self.month = self.kwargs.get("month")
        self.exam_id = get_exam_id(
            self.exam_type,
            self.navigation_or_engineering,
            self.grade,
            self.year,
            self.month,
        )

    def get_queryset(self):
        queryset = super().get_queryset()

        self.get_form_kwargs()

        # フィルタリング
        queryset = queryset.filter(exam__exam_id=self.exam_id)
        return queryset

    def get_context_data(self):
        context = super().get_context_data()
        context.update(
            {
                "exam_type": self.kwargs.get("exam_type"),
                "navigation_or_engineering": self.kwargs.get(
                    "navigation_or_engineering"
                ),
                "grade": self.kwargs.get("grade"),
                "year": self.kwargs.get("year"),
                "month": self.kwargs.get("month"),
            }
        )
        return context


""" 問題画面 """


class QuestionListView(ListView):
    template_name = "kakomon/list_question.html"
    model = Question
    context_object_name = "questions"

    def get_form_kwargs(self):
        self.exam_type = find_key_for_value(self.kwargs.get("exam_type"), EXAMTYPE)
        self.navigation_or_engineering = find_key_for_value(
            self.kwargs.get("navigation_or_engineering"), NAVIGATION_OR_ENGINEERING
        )
        self.grade = find_key_for_value(self.kwargs.get("grade"), GRADE)
        self.year = self.kwargs.get("year")
        self.month = self.kwargs.get("month")
        self.exam_id = get_exam_id(
            self.exam_type,
            self.navigation_or_engineering,
            self.grade,
            self.year,
            self.month,
        )
        self.subject = find_key_for_value(self.kwargs.get("subject"), SUBJECT)

    def get_queryset(self):
        queryset = super().get_queryset()

        self.get_form_kwargs()

        # フィルタリング
        queryset = queryset.filter(
            subject__exam__exam_id=self.exam_id, subject__name=self.subject
        )
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(
            {
                "exam_type": self.kwargs.get("exam_type"),
                "navigation_or_engineering": self.kwargs.get(
                    "navigation_or_engineering"
                ),
                "grade": self.kwargs.get("grade"),
                "year": self.kwargs.get("year"),
                "month": self.kwargs.get("month"),
                "subject": self.kwargs.get("subject"),
            }
        )
        return context

from django.views.generic import TemplateView, ListView, CreateView
from django.urls import reverse_lazy
from .constants import EXAMTYPE, NAVIGATION_OR_MECHANISM, GRADE, SUBJECT
from .functions import find_key_for_value, get_exam_id
from .forms import ExamForm, SubjectForm, QuestionForm
from .models import Exam, Subject, Question

"""Top画面"""
class IndexView(TemplateView):
    template_name = 'kakomon/index.html'


"""管理メニュー"""
class ManagementView(TemplateView):
    template_name = 'kakomon/management.html'



""" 試験画面 """
class ExamListView(ListView):
    template_name = 'kakomon/list_exam.html'
    model = Exam
    context_object_name = 'exams'

    def get_form_kwargs(self):
        self.exam_type = find_key_for_value(self.kwargs.get('exam_type'), EXAMTYPE)
        self.navigation_or_mechanism = find_key_for_value(self.kwargs.get('navigation_or_mechanism'), NAVIGATION_OR_MECHANISM)
        self.grade = find_key_for_value(self.kwargs.get('grade'), GRADE)
    
    def get_queryset(self):
        queryset = super().get_queryset()

        self.get_form_kwargs()

        # フィルタリング
        queryset = queryset.filter(
            exam_type = self.exam_type,
            navigation_or_mechanism = self.navigation_or_mechanism,
            grade = self.grade,
        )

        # 日付が新しい順で表示
        queryset = queryset.order_by('-date')
        return queryset
    

""" 科目画面 """
class SubjectListView(ListView):
    template_name = 'kakomon/list_subject.html'
    model = Subject
    context_object_name = 'subjects'

    def get_form_kwargs(self):
        self.exam_type = find_key_for_value(self.kwargs.get('exam_type'), EXAMTYPE)
        self.navigation_or_mechanism = find_key_for_value(self.kwargs.get('navigation_or_mechanism'), NAVIGATION_OR_MECHANISM)
        self.grade = find_key_for_value(self.kwargs.get('grade'), GRADE)
        self.year = self.kwargs.get('year')
        self.month = self.kwargs.get('month')
        self.exam_id = get_exam_id(self.exam_type, self.navigation_or_mechanism, self.grade, self.year, self.month)

    def get_queryset(self):
        queryset = super().get_queryset()

        self.get_form_kwargs()

        # フィルタリング
        queryset = queryset.filter(
            exam__exam_id = self.exam_id
        )
        return queryset


""" 問題画面 """
class QuestionListView(ListView):
    template_name = 'kakomon/list_question.html'
    model = Question
    context_object_name = 'questions'

    def get_form_kwargs(self):
        self.exam_type = find_key_for_value(self.kwargs.get('exam_type'), EXAMTYPE)
        self.navigation_or_mechanism = find_key_for_value(self.kwargs.get('navigation_or_mechanism'), NAVIGATION_OR_MECHANISM)
        self.grade = find_key_for_value(self.kwargs.get('grade'), GRADE)
        self.year = self.kwargs.get('year')
        self.month = self.kwargs.get('month')
        self.exam_id = get_exam_id(self.exam_type, self.navigation_or_mechanism, self.grade, self.year, self.month)
        self.subject = find_key_for_value(self.kwargs.get('subject'), SUBJECT)
    
    def get_queryset(self):
        queryset = super().get_queryset()

        self.get_form_kwargs()

        # フィルタリング
        queryset = queryset.filter(
            subject__exam__exam_id = self.exam_id,
            subject__name = self.subject
        )
        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['year'] = self.year
        context['month'] = self.month
        return context


"""試験登録"""
class ExamCreateView(CreateView):
    model = Exam
    form_class = ExamForm
    template_name = 'kakomon/create_exam.html'
    success_url = reverse_lazy('kakomon:management')

    def test_func(self):
        return self.request.user.is_contribute


"""科目登録"""
class SubjectCreateView(CreateView):
    model = Subject
    form_class = SubjectForm
    template_name = 'kakomon/create_subject.html'
    success_url = reverse_lazy('kakomon:management')

    def test_func(self):
        return self.request.user.is_contribute


"""質問登録"""
class QuestionCreateView(CreateView):
    model = Question
    form_class = QuestionForm
    template_name = 'kakomon/create_question.html'
    success_url = reverse_lazy('kakomon:management')

    def test_func(self):
        return self.request.user.is_contribute
from django.views.generic import TemplateView, ListView
from .models import Exam, Subject, Question
from .constants import EXAMTYPE, NAVIGATION_OR_MECHANISM, GRADE, SUBJECT, SHOMON

# 関数
def find_key_for_value(value, tuple_list):
    for key, val in tuple_list:
        if val == value:
            return key
    return None

def get_exam_id(examtype, navigation_or_mechanism, grade, year, month):
    exam_id = []
    # 試験種類（1:筆記, 2:口述）
    if examtype == 'writing':
        exam_id.append(1)
    else:
        exam_id.append(2)
    # 航機種類（1:航海, 2:機械）
    if navigation_or_mechanism == 'navigation':
        exam_id.append(1)
    else:
        exam_id.append(2)
    # 級名（1:1級, 2:２級, 3:3級）
    if grade == 'grade1':
        exam_id.append(1)
    elif grade == 'grade2':
        exam_id.append(2)
    else:
        exam_id.append(3)
    # 年度
    exam_id.append(year)
    # 月度
    exam_id.append(str(month).zfill(2))
    exam_id = ''.join(str(i) for i in exam_id)
    return exam_id

def get_shomon(shomon, SHOMON:dict):
    return SHOMON.get(shomon)


class IndexView(TemplateView):
    template_name = 'kakomon/index.html'

""" 試験画面 """
class ExamListView(ListView):
    template_name = 'kakomon/exam_list.html'
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
    template_name = 'kakomon/subject_list.html'
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
    template_name = 'kakomon/question_list.html'
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
    
from django.urls import path
from . import views

app_name = 'kakomon'

urlpatterns = [
    path('index', views.IndexView.as_view(), name='index'),
    path('<exam_type>/<navigation_or_mechanism>/<grade>', views.ExamListView.as_view(), name='exam_list'),
    path('<exam_type>/<navigation_or_mechanism>/<grade>/<int:year>/<int:month>', views.SubjectListView.as_view(), name='subject_list'),
    path('<exam_type>/<navigation_or_mechanism>/<grade>/<int:year>/<int:month>/<subject>', views.QuestionListView.as_view(), name='question_list'),
]
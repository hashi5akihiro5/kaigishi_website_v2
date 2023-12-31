from django.urls import path
from . import views

app_name = 'kakomon'

urlpatterns = [
    path('index', views.IndexView.as_view(), name='index'),
    path('management', views.ManagementView.as_view(), name='management'),
    path('management/create/exam', views.ExamCreateView.as_view(), name='create_exam'),
    path('<exam_type>/<navigation_or_mechanism>/<grade>', views.ExamListView.as_view(), name='exam_list'),
    path('<exam_type>/<navigation_or_mechanism>/<grade>/<int:year>/<int:month>', views.SubjectListView.as_view(), name='subject_list'),
    path('<exam_type>/<navigation_or_mechanism>/<grade>/<int:year>/<int:month>/<subject>', views.QuestionListView.as_view(), name='question_list'),
]
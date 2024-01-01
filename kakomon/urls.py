from django.urls import path
from . import views

app_name = 'kakomon'

urlpatterns = [
    path('index', views.IndexView.as_view(), name='index'),
    path('management', views.ManagementView.as_view(), name='management'),
    path('management/create/exam', views.ExamCreateView.as_view(), name='create_exam'),
    path('management/create/subject', views.SubjectCreateView.as_view(), name='create_subject'),
    path('management/create/question', views.QuestionCreateView.as_view(), name='create_question'),
    path('<exam_type>/<navigation_or_mechanism>/<grade>', views.ExamListView.as_view(), name='list_exam'),
    path('<exam_type>/<navigation_or_mechanism>/<grade>/<int:year>/<int:month>', views.SubjectListView.as_view(), name='list_subject'),
    path('<exam_type>/<navigation_or_mechanism>/<grade>/<int:year>/<int:month>/<subject>', views.QuestionListView.as_view(), name='list_question'),
]
from django.urls import path
from . import views

app_name = 'kakomon'

urlpatterns = [
    path('index', views.IndexView.as_view(), name='index'),
    path('management', views.ManagementView.as_view(), name='management'),
    path('management/create/exam', views.ExamCreateView.as_view(), name='create_exam'),
    path('management/create/subject', views.SubjectCreateView.as_view(), name='create_subject'),
    path('management/create/question', views.QuestionCreateView.as_view(), name='create_question'),
    path('management/edit/exam/list', views.ExamEditListView.as_view(), name='edit_exam_list'),
    path('management/edit/subject/list', views.SubjectEditListView.as_view(), name='edit_subject_list'),
    path('management/edit/quesiton/list', views.QuestionEditListView.as_view(), name='edit_question_list'),
    path('management/edit/exam/<int:pk>', views.ExamEditView.as_view(), name='edit_exam'),
    path('management/edit/subject/<int:pk>', views.SubjectEditView.as_view(), name='edit_subject'),
    path('management/edit/question/<int:pk>', views.QuestionEditView.as_view(), name='edit_question'),
    path('<exam_type>/<navigation_or_mechanism>/<grade>', views.ExamListView.as_view(), name='list_exam'),
    path('<exam_type>/<navigation_or_mechanism>/<grade>/<int:year>/<int:month>', views.SubjectListView.as_view(), name='list_subject'),
    path('<exam_type>/<navigation_or_mechanism>/<grade>/<int:year>/<int:month>/<subject>', views.QuestionListView.as_view(), name='list_question'),
]
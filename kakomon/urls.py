from django.urls import path

from . import views

app_name = "kakomon"

urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path(
        "<exam_type>/<navigation_or_engineering>/<grade>/",
        views.ExamListView.as_view(),
        name="list_exam",
    ),
    path(
        "<exam_type>/<navigation_or_engineering>/<grade>/<int:year>/<int:month>/",
        views.SubjectListView.as_view(),
        name="list_subject",
    ),
    path(
        "<exam_type>/<navigation_or_engineering>/<grade>/<int:year>/<int:month>/<subject>/",
        views.QuestionListView.as_view(),
        name="list_question",
    ),
]

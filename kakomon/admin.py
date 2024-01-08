from django.contrib import admin
from .models import Exam, Subject, Question


class ExamAdmin(admin.ModelAdmin):
    list_display = ("date", "grade", "navigation_or_mechanism", "exam_type", )
    list_filter = ("exam_type", "grade", "navigation_or_mechanism",) 
    search_fields = ("exam_id",)
    date_hierarchy = "date"


class SubjectAdmin(admin.ModelAdmin):
    list_display = ("name", "get_date", "get_grade", "get_navigation_or_mechanism", "get_exam_type")
    list_filter = ("exam__exam_type", "exam__grade", "exam__navigation_or_mechanism")
    search_fields = ("name",)
    date_hierarchy = "exam__date"

    def get_date(self, obj):
        return obj.exam.date
    get_date.short_description = '定期'

    def get_grade(self, obj):
        return obj.exam.get_grade_display()
    get_grade.short_description = '級名'

    def get_navigation_or_mechanism(self, obj):
        return obj.exam.get_navigation_or_mechanism_display()
    get_navigation_or_mechanism.short_description = '航海・機関'

    def get_exam_type(self, obj):
        return obj.exam.get_exam_type_display()
    get_exam_type.short_description = '筆記・口述'


class QuestionAdmin(admin.ModelAdmin):
    list_display = ("daimon", "shomon", "edamon", "get_subject", "get_date", "get_grade", "get_navigation_or_mechanism", "get_exam_type")
    list_filter = ("subject__exam__exam_type", "subject__exam__navigation_or_mechanism","subject__exam__grade",  "subject__name", "daimon", "shomon", "edamon")
    search_fields = ("subject__name",)
    date_hierarchy = "subject__exam__date"

    def get_subject(self, obj):
        return obj.subject.get_name_display()
    get_subject.short_description = '科目'

    def get_date(self, obj):
        return obj.subject.exam.date
    get_date.short_description = '定期'

    def get_grade(self, obj):
        return obj.subject.exam.get_grade_display()
    get_grade.short_description = '級名'

    def get_navigation_or_mechanism(self, obj):
        return obj.subject.exam.get_navigation_or_mechanism_display()
    get_navigation_or_mechanism.short_description = '航海・機関'

    def get_exam_type(self, obj):
        return obj.subject.exam.get_exam_type_display()
    get_exam_type.short_description = '筆記・口述'


admin.site.register(Exam, ExamAdmin)
admin.site.register(Subject, SubjectAdmin)
admin.site.register(Question, QuestionAdmin)

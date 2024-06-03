from django.contrib import admin

from .models import Category, Exam, Question, SimilarQuestion, Subject, Tag


class ExamAdmin(admin.ModelAdmin):
    list_display = (
        "date",
        "navigation_or_engineering",
        "grade",
        "exam_type",
    )
    list_filter = (
        "exam_type",
        "grade",
        "navigation_or_engineering",
    )
    search_fields = ("exam_id",)
    date_hierarchy = "date"


class SubjectAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "get_date",
        "get_grade",
        "get_navigation_or_engineering",
        "get_exam_type",
    )
    list_filter = ("exam__exam_type", "exam__grade", "exam__navigation_or_engineering")
    search_fields = ("name",)
    date_hierarchy = "exam__date"

    def get_date(self, obj):
        return obj.exam.date

    get_date.short_description = "定期"

    def get_grade(self, obj):
        return obj.exam.get_grade_display()

    get_grade.short_description = "級名"

    def get_navigation_or_engineering(self, obj):
        return obj.exam.get_navigation_or_engineering_display()

    get_navigation_or_engineering.short_description = "航海・機関"

    def get_exam_type(self, obj):
        return obj.exam.get_exam_type_display()

    get_exam_type.short_description = "筆記・口述"


class QuestionAdmin(admin.ModelAdmin):
    list_display = (
        "daimon",
        "shomon",
        "edamon",
        "get_subject",
        "get_date",
        "get_grade",
        "get_navigation_or_engineering",
        "get_exam_type",
    )
    list_filter = (
        "subject__exam__exam_type",
        "subject__exam__navigation_or_engineering",
        "subject__exam__grade",
        "subject__name",
        "daimon",
        "shomon",
        "edamon",
    )
    search_fields = ("subject__name",)
    date_hierarchy = "subject__exam__date"
    radio_fields = {
        "question_image_position_description_or_question": admin.HORIZONTAL,
        "question_image_position_right_or_under": admin.HORIZONTAL,
        "answer_image_position_right_or_under": admin.HORIZONTAL,
    }

    def get_subject(self, obj):
        return obj.subject.get_name_display()

    get_subject.short_description = "科目"

    def get_date(self, obj):
        return obj.subject.exam.date

    get_date.short_description = "定期"

    def get_grade(self, obj):
        return obj.subject.exam.get_grade_display()

    get_grade.short_description = "級名"

    def get_navigation_or_engineering(self, obj):
        return obj.subject.exam.get_navigation_or_engineering_display()

    get_navigation_or_engineering.short_description = "航海・機関"

    def get_exam_type(self, obj):
        return obj.subject.exam.get_exam_type_display()

    get_exam_type.short_description = "筆記・口述"


class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name")


class TagAdmin(admin.ModelAdmin):
    list_display = ("id", "name")


class SimilarQuestionAdmin(admin.ModelAdmin):
    list_display = ("similarity_id", "source_question")
    list_filter = ("similarity_id",)


admin.site.register(Exam, ExamAdmin)
admin.site.register(Subject, SubjectAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(SimilarQuestion, SimilarQuestionAdmin)

from django.db import models

from .constants import (
    EXAMTYPE,
    GRADE,
    IMG_DESCRIPTION_OR_QUESTION,
    IMG_RIGHT_OR_UNDER,
    NAVIGATION_OR_ENGINEERING,
    SHOMON,
    SUBJECT,
    SUBJECT_CHOICES,
)
from .functions import default_exam_id, get_file_path, get_image_upload_path

"""試験モデル"""


class Exam(models.Model):
    exam_id = models.IntegerField(default=default_exam_id)
    date = models.DateField(verbose_name="定期")
    exam_type = models.CharField(
        verbose_name="筆記・口述", choices=EXAMTYPE, max_length=8
    )
    navigation_or_engineering = models.CharField(
        verbose_name="航海・機関", choices=NAVIGATION_OR_ENGINEERING, max_length=11
    )
    grade = models.CharField(verbose_name="級名", choices=GRADE, max_length=6)

    def __str__(self):
        return f"{self.date.year}年 {self.date.month}月 {self.get_exam_type_display()} {self.get_navigation_or_engineering_display()} {self.get_grade_display()}"

    class Meta:
        ordering = ["-date", "-navigation_or_engineering", "grade"]
        verbose_name = "試験"
        verbose_name_plural = "1.試験"


"""科目モデル"""


class Subject(models.Model):
    exam = models.ForeignKey(
        Exam, on_delete=models.CASCADE, related_name="subjects", verbose_name="試験"
    )
    name = models.CharField(verbose_name="科目", choices=SUBJECT, max_length=12)
    name_order = models.IntegerField(
        verbose_name="科目順序", choices=[(v, k) for k, v in SUBJECT_CHOICES.items()]
    )
    file_path = models.FileField(
        verbose_name="PDF", upload_to=get_file_path, null=True, blank=True
    )

    def save(self, *args, **kwargs):
        self.name_order = SUBJECT_CHOICES.get(self.name, 0)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.exam.date.year}年 {self.exam.date.month}月 {self.exam.get_exam_type_display()} {self.exam.get_navigation_or_engineering_display()} {self.exam.get_grade_display()} {self.get_name_display()}"

    class Meta:
        ordering = [
            "-exam__date",
            "-exam__navigation_or_engineering",
            "exam__grade",
            "name_order",
        ]
        verbose_name = "科目"
        verbose_name_plural = "2.科目"


"""問題モデル"""


class Question(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, verbose_name="科目")
    daimon = models.PositiveSmallIntegerField(verbose_name="大問")
    daimon_description = models.TextField(
        verbose_name="大問説明", null=True, blank=True
    )
    shomon = models.IntegerField(
        verbose_name="小問", choices=SHOMON, null=True, blank=True
    )
    shomon_description = models.TextField(
        verbose_name="小問説明", null=True, blank=True
    )
    edamon = models.PositiveSmallIntegerField(
        verbose_name="枝問", null=True, blank=True
    )
    question_image = models.ImageField(
        verbose_name="問題画像", upload_to=get_image_upload_path, null=True, blank=True
    )
    question_image_position_description_or_question = models.CharField(
        verbose_name="問題画像配置1",
        choices=IMG_DESCRIPTION_OR_QUESTION,
        max_length=11,
        default=None,
        null=True,
        blank=True,
    )
    question_image_position_right_or_under = models.CharField(
        verbose_name="問題画像配置2",
        choices=IMG_RIGHT_OR_UNDER,
        max_length=5,
        default=None,
        null=True,
        blank=True,
    )
    question_no_indent = models.BooleanField(
        verbose_name="問題インデントなし", default=False
    )
    question = models.TextField(verbose_name="問題")
    answer_image = models.ImageField(
        verbose_name="解答画像", upload_to=get_image_upload_path, null=True, blank=True
    )
    answer_image_position_right_or_under = models.CharField(
        verbose_name="解答画像配置",
        choices=IMG_RIGHT_OR_UNDER,
        max_length=5,
        default=None,
        null=True,
        blank=True,
    )
    answer_no_indent = models.BooleanField(
        verbose_name="解答インデントなし", default=False
    )
    answer = models.TextField(verbose_name="解答")
    similar_questions = models.ManyToManyField(
        "self",
        through="SimilarQuestion",
        related_name="related_similar_questions",
        symmetrical=False,
        verbose_name="類似問題",
        blank=True,
    )

    def __str__(self):
        if self.edamon:
            return f"{self.subject.exam.date.year}年 {self.subject.exam.date.month}月 {self.subject.exam.get_exam_type_display()} {self.subject.exam.get_navigation_or_engineering_display()} {self.subject.exam.get_grade_display()} {self.subject.get_name_display()}_大問{self.daimon}_小問{self.shomon}_枝問{self.edamon}"
        else:
            return f"{self.subject.exam.date.year}年 {self.subject.exam.date.month}月 {self.subject.exam.get_exam_type_display()} {self.subject.exam.get_navigation_or_engineering_display()} {self.subject.exam.get_grade_display()} {self.subject.get_name_display()}_大問{self.daimon}_小問{self.shomon}"

    class Meta:
        ordering = [
            "-subject__exam__date",
            "-subject__exam__navigation_or_engineering",
            "subject__exam__grade",
            "subject__name_order",
            "daimon",
            "shomon",
            "edamon",
        ]
        verbose_name = "問題"
        verbose_name_plural = "3.問題"


"""カテゴリーモデル"""


class Category(models.Model):
    name = models.CharField(verbose_name="カテゴリー", max_length=255)

    class Meta:
        verbose_name = "カテゴリー"
        verbose_name_plural = "4.カテゴリー"

    def __str__(self):
        return self.name


"""タグモデル"""


class Tag(models.Model):
    name = models.CharField(verbose_name="タグ", max_length=255)

    class Meta:
        verbose_name = "タグ"
        verbose_name_plural = "5.タグ"

    def __str__(self):
        return self.name


"""類似問題モデル(中間テーブル)"""


class SimilarQuestion(models.Model):
    similarity_id = models.IntegerField(verbose_name="類似性ID", null=True, blank=True)
    similarity_score = models.IntegerField(
        verbose_name="類似度スコア", null=True, blank=True
    )
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, null=True, blank=True
    )
    tags = models.ManyToManyField(Tag, verbose_name="タグ", blank=True)
    source_question = models.ForeignKey(
        Question, verbose_name="元問題", related_name="source", on_delete=models.CASCADE
    )
    similar_question = models.ForeignKey(
        Question,
        verbose_name="類似問題",
        related_name="similar",
        on_delete=models.CASCADE,
    )
    similarity_reason = models.TextField(verbose_name="類似理由", null=True, blank=True)

    class Meta:
        unique_together = ("source_question", "similar_question")
        verbose_name = "類似問題"
        verbose_name_plural = "6.類似問題"

    def __str__(self):
        return f"{self.source_question} -> {self.similar_question}"

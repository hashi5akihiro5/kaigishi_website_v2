from .constants import EXAMTYPE, NAVIGATION_OR_MECHANISM, GRADE, SUBJECT, SHOMON, SUBJECT_CHOICES
from datetime import date
from django.db import models
import os


"""試験モデル"""
class Exam(models.Model):
    def get_exam_id():
        today = date.today()
        exam_id = "".join(
            [str(1),# 筆記口述種類（1:筆記, 2:口述）
            str(1),# 航機種類（1:航海, 2:機関）
            str(1),# 級名(1:1級, 2:2級, 3:3級)
            str(today.year),# 年度
            str(today.month),# 月度
            ])
        return exam_id
    
    exam_id = models.IntegerField(default=get_exam_id)
    date = models.DateField(verbose_name='定期')
    exam_type = models.CharField(verbose_name="筆記・口述", choices=EXAMTYPE, max_length=8)
    grade = models.CharField(verbose_name="級名", choices=GRADE, max_length=6)
    navigation_or_mechanism = models.CharField(verbose_name="航海・機関", choices=NAVIGATION_OR_MECHANISM, max_length=10)
    
    class Meta:
        ordering = ["-exam_id"]


"""科目モデル"""
class Subject(models.Model):
    def get_file_path(instance, filename):
        return os.path.join(
            str('PDF'),
            str(instance.exam.get_exam_type_display()),
            str(instance.exam.get_navigation_or_mechanism_display()),
            str(instance.exam.get_grade_display()),
            str(instance.exam.date.year),
            str(instance.exam.date.month),
            str(instance.get_name_display()),
            filename
        )
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE, related_name='subjects', verbose_name='試験')
    name = models.CharField(verbose_name="科目", choices=SUBJECT, max_length=10)
    name_order = models.IntegerField(verbose_name="科目順序", choices=[(v, k) for k, v in SUBJECT_CHOICES.items()])
    file_path = models.FileField(verbose_name="PDF", upload_to=get_file_path, null=True, blank=True)

    def save(self, *args, **kwargs):
        self.name_order = SUBJECT_CHOICES.get(self.name, 0)
        super().save(*args, **kwargs)
    
    class Meta:
        ordering = ["-exam__exam_id", "name_order"]
    

"""問題モデル"""
class Question(models.Model):
    def get_image_upload_path(instance, filename):
        return os.path.join(
            str(instance.subject.exam.get_exam_type_display()),
            str(instance.subject.exam.get_navigation_or_mechanism_display()),
            str(instance.subject.exam.get_grade_display()),
            str(instance.subject.exam.date.year),
            str(instance.subject.exam.date.month),
            str(instance.subject.get_name_display()),
            f'大問{str(instance.daimon)}',
            filename
        )
        
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, verbose_name='科目')
    question_id = models.IntegerField(verbose_name="問題ID", default=0, null=True, blank=True)
    daimon = models.PositiveSmallIntegerField(verbose_name="大問")
    shomon = models.IntegerField(verbose_name="小問", choices=SHOMON)
    edamon = models.PositiveSmallIntegerField(verbose_name="枝問", null=True, blank=True)
    similar_questions = models.ManyToManyField('self', verbose_name="類似問題", blank=True)
    question_description = models.TextField(verbose_name="問題説明", null=True, blank=True)
    question_image = models.ImageField(verbose_name="問題画像", upload_to=get_image_upload_path, null=True, blank=True)
    question = models.TextField(verbose_name="問題")
    answer_no_indent = models.BooleanField(verbose_name="解答インデント有無", default=False)
    answer_image = models.ImageField(verbose_name="解答画像", upload_to=get_image_upload_path, null=True, blank=True)
    answer = models.TextField(verbose_name="解答")
    
    class Meta:
        ordering = ["subject", "daimon", "shomon", "edamon"]
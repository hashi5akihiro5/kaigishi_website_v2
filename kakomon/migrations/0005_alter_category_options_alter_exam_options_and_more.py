# Generated by Django 4.2.7 on 2024-08-04 03:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('kakomon', '0004_alter_exam_options_alter_question_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'カテゴリー', 'verbose_name_plural': '1.カテゴリー'},
        ),
        migrations.AlterModelOptions(
            name='exam',
            options={'ordering': ['-date', '-navigation_or_engineering', 'grade'], 'verbose_name': '試験', 'verbose_name_plural': '3.試験'},
        ),
        migrations.AlterModelOptions(
            name='question',
            options={'ordering': ['-subject__exam__date', '-subject__exam__navigation_or_engineering', 'subject__exam__grade', 'subject__name_order', 'daimon', 'shomon', 'edamon'], 'verbose_name': '問題', 'verbose_name_plural': '5.問題'},
        ),
        migrations.AlterModelOptions(
            name='subject',
            options={'ordering': ['-exam__date', '-exam__navigation_or_engineering', 'exam__grade', 'name_order'], 'verbose_name': '科目', 'verbose_name_plural': '4.科目'},
        ),
        migrations.AlterModelOptions(
            name='tag',
            options={'verbose_name': 'タグ', 'verbose_name_plural': '2.タグ'},
        ),
        migrations.AddField(
            model_name='question',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='kakomon.category'),
        ),
        migrations.AddField(
            model_name='question',
            name='tags',
            field=models.ManyToManyField(blank=True, to='kakomon.tag'),
        ),
    ]
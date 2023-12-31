# Generated by Django 4.2.7 on 2023-12-28 09:03

from django.db import migrations, models
import kakomon.models


class Migration(migrations.Migration):

    dependencies = [
        ('kakomon', '0003_alter_subject_name_order'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='exam',
            options={'ordering': ['-exam_id']},
        ),
        migrations.AlterModelOptions(
            name='subject',
            options={'ordering': ['-exam__exam_id', 'name_order']},
        ),
        migrations.AddField(
            model_name='question',
            name='question_id',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='問題ID'),
        ),
        migrations.AlterField(
            model_name='question',
            name='answer_image',
            field=models.ImageField(blank=True, null=True, upload_to=kakomon.models.Question.get_image_upload_path, verbose_name='解答画像'),
        ),
        migrations.AlterField(
            model_name='question',
            name='question_image',
            field=models.ImageField(blank=True, null=True, upload_to=kakomon.models.Question.get_image_upload_path, verbose_name='問題画像'),
        ),
    ]

# Generated by Django 4.2.7 on 2024-01-27 10:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kakomon', '0008_rename_question_description_question_description_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='shomon',
            field=models.IntegerField(blank=True, choices=[(1, '一'), (2, '二'), (3, '三'), (4, '四'), (5, '五')], null=True, verbose_name='小問'),
        ),
    ]

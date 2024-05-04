# Generated by Django 4.2.7 on 2024-03-28 03:24

from django.db import migrations, models
import django.db.models.deletion
import kakomon.functions


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='カテゴリー')),
            ],
            options={
                'verbose_name': 'カテゴリー',
                'verbose_name_plural': '4.カテゴリー',
            },
        ),
        migrations.CreateModel(
            name='Exam',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('exam_id', models.IntegerField(default=kakomon.functions.default_exam_id)),
                ('date', models.DateField(verbose_name='定期')),
                ('exam_type', models.CharField(choices=[('writing', '筆記'), ('speaking', '口述')], max_length=8, verbose_name='筆記・口述')),
                ('grade', models.CharField(choices=[('grade1', '1級'), ('grade2', '2級'), ('grade3', '3級')], max_length=6, verbose_name='級名')),
                ('navigation_or_mechanism', models.CharField(choices=[('navigation', '航海'), ('mechanism', '機関')], max_length=10, verbose_name='航海・機関')),
            ],
            options={
                'verbose_name': '試験',
                'verbose_name_plural': '1.試験',
                'ordering': ['-date', '-navigation_or_mechanism'],
            },
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('daimon', models.PositiveSmallIntegerField(verbose_name='大問')),
                ('daimon_description', models.TextField(blank=True, null=True, verbose_name='大問説明')),
                ('shomon', models.IntegerField(blank=True, choices=[(1, '一'), (2, '二'), (3, '三'), (4, '四'), (5, '五')], null=True, verbose_name='小問')),
                ('shomon_description', models.TextField(blank=True, null=True, verbose_name='小問説明')),
                ('edamon', models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='枝問')),
                ('question_image', models.ImageField(blank=True, null=True, upload_to=kakomon.functions.get_image_upload_path, verbose_name='問題画像')),
                ('question_image_position_description_or_question', models.CharField(blank=True, choices=[('description', '説明'), ('question', '問題')], default=None, max_length=11, null=True, verbose_name='問題画像配置1')),
                ('question_image_position_right_or_under', models.CharField(blank=True, choices=[('right', '右'), ('under', '下')], default=None, max_length=5, null=True, verbose_name='問題画像配置2')),
                ('question_no_indent', models.BooleanField(default=False, verbose_name='問題インデントなし')),
                ('question', models.TextField(verbose_name='問題')),
                ('answer_image', models.ImageField(blank=True, null=True, upload_to=kakomon.functions.get_image_upload_path, verbose_name='解答画像')),
                ('answer_image_position_right_or_under', models.CharField(blank=True, choices=[('right', '右'), ('under', '下')], default=None, max_length=5, null=True, verbose_name='解答画像配置')),
                ('answer_no_indent', models.BooleanField(default=False, verbose_name='解答インデントなし')),
                ('answer', models.TextField(verbose_name='解答')),
            ],
            options={
                'verbose_name': '問題',
                'verbose_name_plural': '3.問題',
                'ordering': ['subject', 'daimon', 'shomon', 'edamon'],
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='タグ')),
            ],
            options={
                'verbose_name': 'タグ',
                'verbose_name_plural': '5.タグ',
            },
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('navigation', '航海'), ('operation', '運用'), ('law', '法規'), ('english', '英語'), ('mechanism1', '機関1'), ('mechanism2', '機関2'), ('mechanism3', '機関3'), ('working', '執務一般')], max_length=10, verbose_name='科目')),
                ('name_order', models.IntegerField(choices=[(1, 'navigation'), (2, 'operation'), (3, 'law'), (4, 'english'), (5, 'mechanism1'), (6, 'mechanism2'), (7, 'mechanism3'), (8, 'working')], verbose_name='科目順序')),
                ('file_path', models.FileField(blank=True, null=True, upload_to=kakomon.functions.get_file_path, verbose_name='PDF')),
                ('exam', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subjects', to='kakomon.exam', verbose_name='試験')),
            ],
            options={
                'verbose_name': '科目',
                'verbose_name_plural': '2.科目',
                'ordering': ['-exam__exam_id', 'name_order'],
            },
        ),
        migrations.CreateModel(
            name='SimilarQuestion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('similarity_id', models.IntegerField(blank=True, null=True, verbose_name='類似性ID')),
                ('similarity_score', models.IntegerField(blank=True, null=True, verbose_name='類似度スコア')),
                ('similarity_reason', models.TextField(blank=True, null=True, verbose_name='類似理由')),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='kakomon.category')),
                ('similar_question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='similar', to='kakomon.question', verbose_name='類似問題')),
                ('source_question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='source', to='kakomon.question', verbose_name='元問題')),
                ('tags', models.ManyToManyField(blank=True, to='kakomon.tag', verbose_name='タグ')),
            ],
            options={
                'verbose_name': '類似問題',
                'verbose_name_plural': '6.類似問題',
                'unique_together': {('source_question', 'similar_question')},
            },
        ),
        migrations.AddField(
            model_name='question',
            name='similar_questions',
            field=models.ManyToManyField(blank=True, related_name='related_similar_questions', through='kakomon.SimilarQuestion', to='kakomon.question', verbose_name='類似問題'),
        ),
        migrations.AddField(
            model_name='question',
            name='subject',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kakomon.subject', verbose_name='科目'),
        ),
    ]

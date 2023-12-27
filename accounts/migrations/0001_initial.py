# Generated by Django 4.2.7 on 2023-12-27 09:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(max_length=255, unique=True, verbose_name='Eメールアドレス')),
                ('is_active', models.BooleanField(default=True)),
                ('is_contribute', models.BooleanField(default=False)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
                ('username', models.CharField(blank=True, max_length=100, null=True, verbose_name='ユーザー名')),
                ('last_name', models.CharField(blank=True, max_length=100, null=True, verbose_name='名字')),
                ('first_name', models.CharField(blank=True, max_length=100, null=True, verbose_name='名前')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]

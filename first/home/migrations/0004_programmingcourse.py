# Generated by Django 3.2.13 on 2022-05-26 07:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_language'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProgrammingCourse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('duration', models.CharField(max_length=30)),
                ('fees', models.IntegerField()),
                ('trainer', models.CharField(max_length=20)),
            ],
        ),
    ]

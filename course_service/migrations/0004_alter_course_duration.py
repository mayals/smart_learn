# Generated by Django 4.1 on 2023-03-28 18:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course_service', '0003_rename_instructor_id_course_instructor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='duration',
            field=models.CharField(max_length=30),
        ),
    ]

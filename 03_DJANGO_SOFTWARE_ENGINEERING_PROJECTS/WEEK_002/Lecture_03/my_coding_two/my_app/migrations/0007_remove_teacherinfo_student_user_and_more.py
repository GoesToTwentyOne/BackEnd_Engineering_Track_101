# Generated by Django 4.2.4 on 2023-08-06 15:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0006_studentinfo_teachers'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='teacherinfo',
            name='student_user',
        ),
        migrations.AlterField(
            model_name='studentinfo',
            name='teachers',
            field=models.ManyToManyField(to='my_app.teacherinfo'),
        ),
    ]
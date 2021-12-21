# Generated by Django 4.0 on 2021-12-18 01:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('past_questions', '0004_remove_faculty_department_faculty_department'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='faculty',
            name='department',
        ),
        migrations.AddField(
            model_name='department',
            name='faculty',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='past_questions.faculty'),
        ),
    ]
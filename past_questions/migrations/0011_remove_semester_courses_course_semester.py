# Generated by Django 4.0 on 2021-12-18 23:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('past_questions', '0010_remove_year_level_level_year'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='semester',
            name='courses',
        ),
        migrations.AddField(
            model_name='course',
            name='semester',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='past_questions.semester'),
        ),
    ]

# Generated by Django 4.0 on 2021-12-21 01:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('past_questions', '0022_alter_faculty_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='department',
            name='faculty',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='past_questions.faculty'),
        ),
    ]
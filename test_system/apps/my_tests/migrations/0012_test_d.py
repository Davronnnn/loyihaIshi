# Generated by Django 3.0.7 on 2020-07-05 06:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_tests', '0011_remove_student_validator'),
    ]

    operations = [
        migrations.AddField(
            model_name='test',
            name='D',
            field=models.CharField(max_length=60, null=True),
        ),
    ]
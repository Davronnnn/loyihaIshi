# Generated by Django 2.2.7 on 2020-10-02 10:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_tests', '0020_test_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='is_student',
            field=models.BooleanField(null=True),
        ),
    ]

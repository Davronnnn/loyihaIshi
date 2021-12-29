# Generated by Django 3.0.7 on 2020-06-29 07:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_tests', '0006_test_question'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sinflarfanlar',
            name='fanlar',
            field=models.CharField(choices=[('Ona tili', 'Ona tili'), ('Adabiyot', 'Adabiyot'), ('Fizika', 'Fizika'), ('Algebra', 'Algebra'), ('Rus tili', 'Rus tili'), ('Kimyo', 'Kimyo'), ('Biologiya', 'Biologiya'), ('Informatika', 'Informatika'), ('Ingliz tili', 'Ingliz tili'), ('Geometriya', 'Geometriya')], max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='sinflarfanlar',
            name='sinf',
            field=models.CharField(choices=[('9', '9'), ('10', '10'), ('11', '11')], max_length=2, null=True),
        ),
    ]

# Generated by Django 3.0.7 on 2020-07-02 16:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('my_tests', '0008_auto_20200630_1802'),
    ]

    operations = [
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('viloyat', models.CharField(max_length=20, null=True)),
                ('school', models.CharField(max_length=20, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='student',
            name='school',
        ),
        migrations.AddField(
            model_name='student',
            name='student',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='my_tests.School'),
            preserve_default=False,
        ),
    ]

# Generated by Django 3.0.3 on 2020-02-09 14:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('test_cases', '0002_auto_20200207_1604'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tracker',
            name='email',
        ),
        migrations.RemoveField(
            model_name='tracker',
            name='module',
        ),
        migrations.RemoveField(
            model_name='tracker',
            name='tester',
        ),
        migrations.AlterField(
            model_name='tracker',
            name='kainos_id',
            field=models.CharField(max_length=200, null=True, verbose_name='Kainos Automated TC ID'),
        ),
        migrations.AlterField(
            model_name='tracker',
            name='scenario',
            field=models.CharField(max_length=1000, null=True, verbose_name='Scenario'),
        ),
    ]

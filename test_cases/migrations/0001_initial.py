# Generated by Django 3.0.3 on 2020-02-07 07:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cases',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('test_case', models.CharField(max_length=1000)),
                ('kainos_id', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Tracker',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tester', models.CharField(max_length=100)),
                ('last_modified', models.DateTimeField(verbose_name='Last Modified')),
                ('result', models.BooleanField()),
                ('case', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='test_cases.Cases')),
            ],
        ),
    ]

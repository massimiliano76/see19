# Generated by Django 3.0.4 on 2020-05-30 21:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('casestudy', '0056_remove_tests_tests'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tests',
            name='test_test',
        ),
        migrations.AddField(
            model_name='tests',
            name='float_test',
            field=models.FloatField(null=True, verbose_name='Count'),
        ),
    ]
# Generated by Django 3.0.4 on 2020-03-28 22:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NewCases',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('region', models.CharField(max_length=40, verbose_name='Region')),
                ('date', models.DateTimeField(verbose_name='Date')),
                ('number', models.PositiveSmallIntegerField(verbose_name='Count')),
            ],
        ),
    ]
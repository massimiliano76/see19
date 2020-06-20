# Generated by Django 3.0.4 on 2020-04-28 21:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('casestudy', '0049_auto_20200427_2235'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='strindex',
            name='s1',
        ),
        migrations.RemoveField(
            model_name='strindex',
            name='s10',
        ),
        migrations.RemoveField(
            model_name='strindex',
            name='s11',
        ),
        migrations.RemoveField(
            model_name='strindex',
            name='s12',
        ),
        migrations.RemoveField(
            model_name='strindex',
            name='s13',
        ),
        migrations.RemoveField(
            model_name='strindex',
            name='s2',
        ),
        migrations.RemoveField(
            model_name='strindex',
            name='s3',
        ),
        migrations.RemoveField(
            model_name='strindex',
            name='s4',
        ),
        migrations.RemoveField(
            model_name='strindex',
            name='s5',
        ),
        migrations.RemoveField(
            model_name='strindex',
            name='s6',
        ),
        migrations.RemoveField(
            model_name='strindex',
            name='s7',
        ),
        migrations.RemoveField(
            model_name='strindex',
            name='s8',
        ),
        migrations.RemoveField(
            model_name='strindex',
            name='s9',
        ),
        migrations.AddField(
            model_name='strindex',
            name='c1',
            field=models.SmallIntegerField(null=True, verbose_name='School Closing'),
        ),
        migrations.AddField(
            model_name='strindex',
            name='c2',
            field=models.SmallIntegerField(null=True, verbose_name='Workplace Closing'),
        ),
        migrations.AddField(
            model_name='strindex',
            name='c3',
            field=models.SmallIntegerField(null=True, verbose_name='Cancel Public Events'),
        ),
        migrations.AddField(
            model_name='strindex',
            name='c4',
            field=models.SmallIntegerField(null=True, verbose_name='Restrictions on Gatherings'),
        ),
        migrations.AddField(
            model_name='strindex',
            name='c5',
            field=models.SmallIntegerField(null=True, verbose_name='Close Public Transport'),
        ),
        migrations.AddField(
            model_name='strindex',
            name='c6',
            field=models.SmallIntegerField(null=True, verbose_name='Stay-at-Home Requirements'),
        ),
        migrations.AddField(
            model_name='strindex',
            name='c7',
            field=models.SmallIntegerField(null=True, verbose_name='Restrictions on Internal Movement'),
        ),
        migrations.AddField(
            model_name='strindex',
            name='c8',
            field=models.SmallIntegerField(null=True, verbose_name='International Travel Controls'),
        ),
        migrations.AddField(
            model_name='strindex',
            name='e1',
            field=models.SmallIntegerField(null=True, verbose_name='Income Support'),
        ),
        migrations.AddField(
            model_name='strindex',
            name='e2',
            field=models.SmallIntegerField(null=True, verbose_name='Debt / Contract Relief'),
        ),
        migrations.AddField(
            model_name='strindex',
            name='e3',
            field=models.SmallIntegerField(null=True, verbose_name='Fiscal Measures'),
        ),
        migrations.AddField(
            model_name='strindex',
            name='e4',
            field=models.SmallIntegerField(null=True, verbose_name='International Support'),
        ),
        migrations.AddField(
            model_name='strindex',
            name='h1',
            field=models.SmallIntegerField(null=True, verbose_name='Public Information Campaigns'),
        ),
        migrations.AddField(
            model_name='strindex',
            name='h2',
            field=models.SmallIntegerField(null=True, verbose_name='Testing Policy'),
        ),
        migrations.AddField(
            model_name='strindex',
            name='h3',
            field=models.SmallIntegerField(null=True, verbose_name='Contact Tracing'),
        ),
        migrations.AddField(
            model_name='strindex',
            name='h4',
            field=models.SmallIntegerField(null=True, verbose_name='Emergency Investment in Health Care'),
        ),
        migrations.AddField(
            model_name='strindex',
            name='h5',
            field=models.SmallIntegerField(null=True, verbose_name='Investment in Vaccines'),
        ),
    ]
# Generated by Django 3.2.4 on 2021-07-13 13:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api_app', '0008_remove_job_runtime_configuration'),
        ('analyzers_manager', '0004_analyzerreport_runtime_configuration'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='analyzerreport',
            unique_together={('analyzer_name', 'job')},
        ),
    ]
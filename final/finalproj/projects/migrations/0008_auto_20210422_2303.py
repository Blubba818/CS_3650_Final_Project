# Generated by Django 3.2 on 2021-04-23 05:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0007_project_date_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='priority',
            field=models.IntegerField(choices=[(5, 'Lowest'), (4, 'Low'), (3, 'Medium'), (2, 'High'), (1, 'Highest')], default=3),
        ),
        migrations.AlterField(
            model_name='project',
            name='status',
            field=models.IntegerField(choices=[(1, 'Incomplete'), (2, 'In-Progress'), (3, 'Complete')], default=1),
        ),
    ]

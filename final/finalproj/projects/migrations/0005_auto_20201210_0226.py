# Generated by Django 2.2 on 2020-12-10 09:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0004_auto_20201210_0205'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='image',
            field=models.ImageField(default='images/project.jpg', upload_to='images/'),
        ),
    ]

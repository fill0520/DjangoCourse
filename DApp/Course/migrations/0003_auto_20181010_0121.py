# Generated by Django 2.1.2 on 2018-10-09 19:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Course', '0002_auto_20181010_0051'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]

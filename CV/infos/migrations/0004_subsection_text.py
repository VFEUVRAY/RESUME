# Generated by Django 3.2 on 2021-04-30 05:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('infos', '0003_auto_20210429_2335'),
    ]

    operations = [
        migrations.AddField(
            model_name='subsection',
            name='text',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]
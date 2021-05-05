# Generated by Django 3.2 on 2021-04-29 09:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('infos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SubSection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('section_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='infos.section')),
            ],
        ),
        migrations.AlterField(
            model_name='paragraph',
            name='section_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='infos.subsection'),
        ),
    ]

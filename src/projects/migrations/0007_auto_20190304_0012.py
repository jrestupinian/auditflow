# Generated by Django 2.1.5 on 2019-03-04 00:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0006_auto_20190225_0440'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='leader',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='people.Person'),
        ),
        migrations.AlterField(
            model_name='task',
            name='assignee',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='people.Person'),
        ),
        migrations.AlterField(
            model_name='task',
            name='project_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='projects.Project'),
        ),
    ]

# Generated by Django 2.1.5 on 2019-02-25 04:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0003_auto_20190225_0420'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='completed',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='task',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='task',
            name='due_date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='task',
            name='start_date',
            field=models.DateField(),
        ),
    ]

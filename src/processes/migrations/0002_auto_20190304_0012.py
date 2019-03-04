# Generated by Django 2.1.5 on 2019-03-04 00:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('processes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='process',
            name='macroprocess_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='processes.MacroProcess'),
        ),
    ]
# Generated by Django 4.2.5 on 2023-09-13 23:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('funcionario', '0001_initial'),
        ('documento', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='documento',
            name='funcionario',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='funcionario.funcionario'),
        ),
    ]

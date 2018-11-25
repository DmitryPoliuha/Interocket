# Generated by Django 2.1.3 on 2018-11-20 19:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_auto_20181118_1006'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='tours',
        ),
        migrations.AddField(
            model_name='order',
            name='tours',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='app.Cart'),
            preserve_default=False,
        ),
    ]

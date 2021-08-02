# Generated by Django 2.2 on 2021-07-27 10:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('PWapp', '0003_list_creator'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='is_moderator',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='list',
            name='creator',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='PWapp.Player'),
        ),
    ]

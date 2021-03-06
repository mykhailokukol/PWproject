# Generated by Django 2.2 on 2021-08-02 16:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('time', models.CharField(default='00:00', max_length=5)),
                ('day', models.CharField(choices=[('Понедельник', 'Понедельник'), ('Вторник', 'Вторник'), ('Среда', 'Среда'), ('Четверг', 'Четверг'), ('Пятница', 'Пятница'), ('Суббота', 'Суббота'), ('Воскресенье', 'Воскресенье')], default='Понедельник', max_length=16)),
                ('week', models.CharField(choices=[('Чётная', 'Чётная'), ('Нечётная', 'Нечётная'), ('Всегда', 'Всегда')], default='Всегда', max_length=12)),
            ],
        ),
        migrations.CreateModel(
            name='Guild',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nickname', models.CharField(max_length=16)),
                ('UID', models.CharField(max_length=64, unique=True)),
                ('CS', models.IntegerField(default=0)),
                ('level', models.CharField(default='1', max_length=8)),
                ('type', models.CharField(choices=[('Лучник', 'Лучник'), ('Маг', 'Маг'), ('Чародей', 'Чародей'), ('Жрец', 'Жрец'), ('Оборотень', 'Оборотень'), ('Убийца', 'Убийца'), ('Воин', 'Воин'), ('Друид', 'Друид')], default='Класс не указан.', max_length=16)),
                ('guild', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='PWapp.Guild')),
            ],
        ),
        migrations.CreateModel(
            name='UserExtended',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_moderator', models.BooleanField(default=False)),
                ('player', models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to='PWapp.Player')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='List',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Список без названия.', max_length=128)),
                ('access', models.CharField(choices=[('all', 'Для всех'), ('guild', 'Для гильдии'), ('me', 'Только для меня')], default='all', max_length=16)),
                ('creator', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('players', models.ManyToManyField(to='PWapp.Player')),
            ],
        ),
    ]

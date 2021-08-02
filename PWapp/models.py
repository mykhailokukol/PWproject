from django.db import models
from django.contrib.auth.models import User
from django.contrib import admin
# from django.utils import timezone

# Create your models here.
DAY_CHOICES = [
    ('Понедельник', 'Понедельник'),
    ('Вторник', 'Вторник'),
    ('Среда', 'Среда'),
    ('Четверг', 'Четверг'),
    ('Пятница', 'Пятница'),
    ('Суббота', 'Суббота'),
    ('Воскресенье', 'Воскресенье'),
]

class UserExtended(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    player = models.OneToOneField('Player', on_delete=models.CASCADE, default=1)
    is_moderator = models.BooleanField(default=False)

    def __str__(self):
        return (('%s - %s') % (self.user.username, self.player))

class Player(models.Model):

    TYPE_CHOICES = [
        ('Лучник', 'Лучник'),
        ('Маг', 'Маг'),
        ('Чародей', 'Чародей'),
        ('Жрец', 'Жрец'),
        ('Оборотень', 'Оборотень'),
        ('Убийца', 'Убийца'),
        ('Воин', 'Воин'),
        ('Друид', 'Друид'),
    ]

    nickname = models.CharField(max_length=16)
    UID = models.CharField(max_length=64, unique=True)
    CS = models.IntegerField(default=0)
    level = models.CharField(max_length=8, default='1')
    type = models.CharField(max_length=16, choices=TYPE_CHOICES, default='Класс не указан.')
    guild = models.ForeignKey('Guild', on_delete=models.CASCADE, default=None)
    # is_moderator = models.BooleanField(default=False)

    def __str__(self):
        return ('%s %s: %s' % (self.type, self.nickname, self.CS))
        # return (self.type, ' ', self.nickname, ': ', self.CS, '.')
        # просто вызванное через жопу, вспоминал, как это делается

class Event(models.Model):
    WEEK_CHOICES = [
        ('Чётная', 'Чётная'),
        ('Нечётная', 'Нечётная'),
        ('Всегда', 'Всегда'),
    ]

    name = models.CharField(max_length=64)
    time = models.CharField(max_length=5, default='00:00')
    day = models.CharField(default='Понедельник', choices=DAY_CHOICES, max_length=10)
    week = models.CharField(default='Всегда', choices=WEEK_CHOICES, max_length=12)

    def __str__(self):
        return self.name

class List(models.Model):
    ACCESS_CHOICES = [
        ('all', 'Для всех'),
        ('guild', 'Для гильдии'),
        ('me', 'Только для меня'),
    ]

    name = models.CharField(max_length=128, default='Список без названия.')
    creator = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    players = models.ManyToManyField('Player')
    access = models.CharField(max_length=16, default='all', choices=ACCESS_CHOICES)
    # created = models.DateTimeField(auto_now_add=True, editable=False)
    # решить проблему с таймзонами

    def __str__(self):
        return self.name

class Guild(models.Model):
    name = models.CharField(max_length=30, blank=True, null=False)

    def __str__(self):
        return self.name

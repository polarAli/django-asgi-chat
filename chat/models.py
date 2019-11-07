from django.db import models
from django.contrib.auth.models import User


class Group(models.Model):
    name = models.CharField(max_length=50)
    users = models.ManyToManyField(User, related_name='chats')


class Message(models.Model):
    sender = models.ForeignKey(User, related_name='messages_sent', on_delete=models.CASCADE)
    text = models.TextField()
    group = models.ForeignKey(Group, related_name='messages', on_delete=models.CASCADE)

from django.db import models
# from phone_field import PhoneField
from django.contrib.auth.models import User


class Goal(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author_goal')
    content = models.CharField(max_length=300)

    def __str__(self):
        return self.content


class Level(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author_level')
    level = models.CharField(max_length=10)

    def __str__(self):
        return self.level


class Email(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author_email')
    email = models.EmailField(max_length = 254)

    def __str__(self):
        return self.email


class Phone(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author_phone')
    phone = models.CharField(max_length=31)

    def __str__(self):
        return self.phone


class Message(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author_message')
    message = models.TextField()

    def __str__(self):
        return self.message

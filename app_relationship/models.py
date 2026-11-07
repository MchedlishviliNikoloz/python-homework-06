from django.db import models

# Create your models here.

class User(models.Model):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=128, unique=True)
    password = models.CharField(max_length=128)

    def __str__(self):
        return self.username

class Profile(models.Model):
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
    bio = models.TextField()
    birth_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Group(models.Model):
    name = models.CharField(max_length=128)
    created_at = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='owned_groups')
    members = models.ManyToManyField(User, related_name='groups')

    def __str__(self):
        return self.name
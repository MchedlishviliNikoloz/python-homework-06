from django.contrib import admin
from app_relationship.models import User, Profile, Group

# Register your models here.
admin.site.register(User)
admin.site.register(Profile)
admin.site.register(Group)
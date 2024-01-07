from django.contrib import admin
from django.contrib.auth.models import User, Group
from .models import Profile, Twitts

class ProfileLine(admin.StackedInline):
    model = Profile

class UserAdmin(admin.ModelAdmin):
    model = User
    fields = ['username']
    inlines = [ProfileLine]

admin.site.unregister(Group)
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(Twitts)
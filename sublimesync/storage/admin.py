# -*- coding: utf-8 -*-
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

from .models import Member
from .models import Package

class MemberInline(admin.StackedInline):
	model = Member
	can_delete = False


class UserAdmin(UserAdmin):
	inlines = (MemberInline,)

admin.site.unregister(User)
admin.site.register(User, UserAdmin)

admin.site.register(Package)
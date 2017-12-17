# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import models
from django.contrib import admin
from forum.models import UserProfile
# Register your models here.

class EntryAdmin(admin.ModelAdmin):
	list_display = ("title", "date")
	
admin.site.register(UserProfile)
admin.site.register(models.WebsitePost, EntryAdmin)
admin.site.register(models.AssignmentPost, EntryAdmin)
admin.site.register(models.SurvivingPost, EntryAdmin)
admin.site.register(models.LectureSlidesPost, EntryAdmin)
admin.site.register(models.ChartsPost, EntryAdmin)
admin.site.register(models.BinaryPost, EntryAdmin)

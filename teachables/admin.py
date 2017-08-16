from django.contrib import admin
from .models import Topic, Lesson, Step

# Register your models here.

class StepInline(admin.StackedInline):
    model = Step

class LessonAdmin(admin.ModelAdmin):
    inlines = [StepInline,]

admin.site.register(Topic)
admin.site.register(Lesson, LessonAdmin)
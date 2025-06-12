from django.contrib import admin

from finkiXP_app.models import Subject, ExamTask, UserProfile


class SubjectAdmin(admin.ModelAdmin):
    pass


class ExamTaskAdmin(admin.ModelAdmin):
    pass


class UserProfileAdmin(admin.ModelAdmin):
    pass


admin.site.register(Subject, SubjectAdmin)
admin.site.register(ExamTask, ExamTaskAdmin)
admin.site.register(UserProfile, UserProfileAdmin)

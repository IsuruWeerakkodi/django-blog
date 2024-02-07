from django.contrib import admin
from blog.models import School, ClassName, AssessmentAreas, Student, Answers, Awards, Subject


# Register your models here.
class SchoolAdmin(admin.ModelAdmin):
    pass


class ClassNameAdmin(admin.ModelAdmin):
    pass


class AssessmentAreasAdmin(admin.ModelAdmin):
    pass


class StudentAdmin(admin.ModelAdmin):
    pass


class AnswersAdmin(admin.ModelAdmin):
    pass


class AwardsAdmin(admin.ModelAdmin):
    pass


class SubjectAdmin(admin.ModelAdmin):
    pass


admin.site.register(School, SchoolAdmin)
admin.site.register(ClassName, ClassNameAdmin)
admin.site.register(AssessmentAreas, AssessmentAreasAdmin)
admin.site.register(Student, StudentAdmin)
admin.site.register(Answers, AnswersAdmin)
admin.site.register(Awards, AwardsAdmin)
admin.site.register(Subject, SubjectAdmin)

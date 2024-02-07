from django.contrib import admin
from blog.models import School, ClassName
# Register your models here.
class SchoolAdmin(admin.ModelAdmin):
    pass

class ClassNameAdmin(admin.ModelAdmin):
    pass

admin.site.register(School, SchoolAdmin)
admin.site.register(ClassName, ClassNameAdmin)

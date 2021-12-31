from django.contrib import admin
from . models import *
from import_export import resources
from import_export.admin import ImportExportModelAdmin
# Register your models here.

admin.site.register(Cv_user)
admin.site.register(Profile)
admin.site.register(Objective)
admin.site.register(Education)
admin.site.register(Experience)
admin.site.register(Skill)
admin.site.register(Activity)
admin.site.register(Additional)
admin.site.register(Certification)
admin.site.register(Language)



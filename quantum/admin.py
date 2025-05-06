from.models import *
from django.contrib import admin

class displayname(admin.ModelAdmin):
    list_display=['SubjectCode','SubjectName','Branch','Semester','pdf']

admin.site.register(BTechQuantum,displayname)
admin.site.register(MBAQuantum,displayname)
admin.site.register(MCAQuantum,displayname)
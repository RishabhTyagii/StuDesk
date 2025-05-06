from.models import *
from django.contrib import admin

class displayname(admin.ModelAdmin):
    list_display=['SubjectCode','SubjectName','Branch','Semester','pdf']

admin.site.register(BTechNotes,displayname)
admin.site.register(MBANotes,displayname)
admin.site.register(MCANotes,displayname)
from.models import *
from django.contrib import admin

class displayname(admin.ModelAdmin):
    list_display=['SubjectCode','SubjectName','Branch','Semester','pdf']

admin.site.register(BTechExamPapers,displayname)
admin.site.register(MBAExamPapers,displayname)
admin.site.register(MCAExamPapers,displayname)
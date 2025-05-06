from django.shortcuts import render
from.models import *
from notes.models import BTechNotes, MBANotes, MCANotes
from exam_papers.models import BTechExamPapers, MBAExamPapers, MCAExamPapers

def indexpage(request): 
    BTechQuantum1=BTechQuantum.objects.all()
    MBAQuantum1=MBAQuantum.objects.all()
    MCAQuantum1=MCAQuantum.objects.all()
    BTechNotes1=BTechNotes.objects.all()
    MBANotes1=MBANotes.objects.all()
    MCANotes1=MCANotes.objects.all()
    BTechExam_paper=BTechExamPapers.objects.all()
    MBAExam_paper=MBAExamPapers.objects.all()
    MCAExam_paper1=MCAExamPapers.objects.all()


    return render(request,'index.html',{'BTechQuantum1':BTechQuantum1,'MBAQuantum1':MBAQuantum1,'MCAQuantum1': MCAQuantum1,'BTechNotes1':BTechNotes1,'MBANotes1':MBANotes1,'MCANotes1': MCANotes1,'BTechExam_paper':BTechExam_paper,'MBAExam_paper':MBAExam_paper,'MCAExam_paper1': MCAExam_paper1}) 
    
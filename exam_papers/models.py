from django.db import models
class BTechExamPapers(models.Model):
    SubjectCode=models.CharField(max_length=100)
    SubjectName = models.CharField(max_length=255)
    provider= models.CharField(max_length=255)
    Branch=models.CharField(max_length=200)   
    Semester=models.CharField(max_length=200)   
    pdf = models.FileField(upload_to='pdfs/exam_paper/btech')
    def __str__(self):
        return self.SubjectName

class MBAExamPapers(models.Model):
    SubjectCode=models.CharField(max_length=100)
    SubjectName = models.CharField(max_length=255)
    provider= models.CharField(max_length=255)
    Branch=models.CharField(max_length=200)   
    Semester=models.CharField(max_length=200)   
    pdf = models.FileField(upload_to='pdfs/exam_paper/mba')
    def __str__(self):
        return self.SubjectName

    
class MCAExamPapers(models.Model):
    SubjectCode=models.CharField(max_length=100)
    SubjectName = models.CharField(max_length=255)
    provider= models.CharField(max_length=255)
    Branch=models.CharField(max_length=200)   
    Semester=models.CharField(max_length=200)   
    pdf = models.FileField(upload_to='pdfs/exam_paper/mca')
    def __str__(self):
        return self.SubjectName

    
                                                     
    
                                                     
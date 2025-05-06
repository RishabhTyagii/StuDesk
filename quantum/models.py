from django.db import models
class BTechQuantum(models.Model):
    SubjectCode=models.CharField(max_length=100)
    SubjectName = models.CharField(max_length=255)
    provider= models.CharField(max_length=255)
    Branch=models.CharField(max_length=200)   
    Semester=models.CharField(max_length=200)   
    pdf = models.FileField(upload_to='pdfs/quantum/btech')
    def __str__(self):
        return self.SubjectName

class MBAQuantum(models.Model):
    SubjectCode=models.CharField(max_length=100)
    SubjectName = models.CharField(max_length=255)
    provider= models.CharField(max_length=255)
    Branch=models.CharField(max_length=200)   
    Semester=models.CharField(max_length=200)   
    pdf = models.FileField(upload_to='pdfs/quantum/mba')
    def __str__(self):
        return self.SubjectName

    
class MCAQuantum(models.Model):
    SubjectCode=models.CharField(max_length=100)
    SubjectName = models.CharField(max_length=255)
    provider= models.CharField(max_length=255)
    Branch=models.CharField(max_length=200)   
    Semester=models.CharField(max_length=200)   
    pdf = models.FileField(upload_to='pdfs/quantum/mca')
    def __str__(self):
        return self.SubjectName

    
                                                     
    
                                                     
from django.db import models
class BTechNotes(models.Model):
    SubjectCode=models.CharField(max_length=100)
    SubjectName = models.CharField(max_length=255)
    provider= models.CharField(max_length=255)  
    Branch=models.CharField(max_length=200)   
    Semester=models.CharField(max_length=200)   
    pdf = models.FileField(upload_to='pdfs/notes/btech')
    def __str__(self):
        return self.SubjectName

class MBANotes(models.Model):
    SubjectCode=models.CharField(max_length=100)
    SubjectName = models.CharField(max_length=255)
    provider= models.CharField(max_length=255)  
    Branch=models.CharField(max_length=200)   
    Semester=models.CharField(max_length=200)   
    pdf = models.FileField(upload_to='pdfs/notes/mba')
    def __str__(self):
        return self.SubjectName
    
class MCANotes(models.Model):
    SubjectCode=models.CharField(max_length=100)
    SubjectName = models.CharField(max_length=255)
    provider= models.CharField(max_length=255)  
    Branch=models.CharField(max_length=200)   
    Semester=models.CharField(max_length=200)   
    pdf = models.FileField(upload_to='pdfs/notes/mca')
    def __str__(self):
        return self.SubjectName

    
                                                     
    
                                                     
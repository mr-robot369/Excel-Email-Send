from django.db import models

class Teacher(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    sheet_name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class ExcelFile(models.Model):
    file = models.FileField(upload_to='excel_files/')
    upload_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.file.name

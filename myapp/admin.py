from django.contrib import admin
from .models import Teacher, ExcelFile
from .utils import process_pdf_and_send_emails, process_sheet_and_send_emails

class TeacherAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'sheet_name')
    list_filter = ('sheet_name',)
    search_fields = ('name', 'email', 'sheet_name')

class ExcelFileAdmin(admin.ModelAdmin):
    list_display = ('file', 'upload_time')
    list_filter = ('upload_time',)
    search_fields = ('file__name', 'upload_time')

    actions = [process_pdf_and_send_emails,process_sheet_and_send_emails]

admin.site.register(Teacher, TeacherAdmin)
admin.site.register(ExcelFile, ExcelFileAdmin)

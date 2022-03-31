from django.contrib import admin
from .models import Bhav, DateBhav, Securities
from import_export.admin import ImportExportModelAdmin

@admin.register(Securities)
class SecuAdmin(ImportExportModelAdmin):
    pass

@admin.register(DateBhav)
class DateBhavAdmin(ImportExportModelAdmin):
    pass

@admin.register(Bhav)
class BhavAdmin(ImportExportModelAdmin):
    pass

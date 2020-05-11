from django.contrib import admin
from .models import Tracker
#from import_export.admin import ImportExportModelAdmin
from . import models
# Register your models here.
@admin.register(Tracker)
class ViewAdmin(ImportExportModelAdmin):
    pass

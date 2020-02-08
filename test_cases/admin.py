from django.contrib import admin
from .models import Tracker
from import_export.admin import ImportExportModelAdmin
# Register your models here.
admin.site.register(Tracker)

class ViewAdmin(ImportExportModelAdmin):
        exclude = ('id', )

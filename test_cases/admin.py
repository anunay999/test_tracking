from django.contrib import admin
from .models import Tracker
from import_export.admin import ImportExportModelAdmin
from import_export import resources
from . import models
# Register your models here.
admin.site.register(Tracker)

class TrackResource(resources.ModelResource):

    class Meta:
        model = Tracker
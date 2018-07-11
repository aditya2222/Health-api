from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import formModel, SnomedTerms
# Register your models here.

admin.site.register(formModel)


@admin.register(SnomedTerms)
class PersonAdmin(ImportExportModelAdmin):
    pass
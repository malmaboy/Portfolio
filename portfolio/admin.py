from django.contrib import admin
import portfolio.models as models

# Register your models here.

admin.site.register(models.Subject)
admin.site.register(models.Projects)
admin.site.register(models.ProgrammingLanguages)
admin.site.register(models.Topics)
admin.site.register(models.NonProgrammingLanguages)
admin.site.register(models.Description)

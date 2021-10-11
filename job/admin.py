from django.contrib import admin
from .models import job, category, Apply
# Register your models here.

admin.site.register(job)
admin.site.register(category)
admin.site.register(Apply)
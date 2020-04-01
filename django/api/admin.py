from django.contrib import admin
from .models import Plan, SpecificPlanList, Task

# Register your models here.
admin.site.register(Plan)
admin.site.register(SpecificPlanList)
admin.site.register(Task)
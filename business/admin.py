from django.contrib import admin
from .models import User, role, lead, activity, task

# Register your models here.
admin.site.register(User)
admin.site.register(role)
admin.site.register(lead)
admin.site.register(activity)
admin.site.register(task)
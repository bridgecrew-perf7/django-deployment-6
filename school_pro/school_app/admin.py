from django.contrib import admin
from school_app.models import UserProfile,School,Student

# Register your models here.

admin.site.register(UserProfile)
admin.site.register(School)
admin.site.register(Student)

from django.contrib import admin

# Register your models here.
from .models import *
admin.site.register(Courses)
admin.site.register(Customer)
admin.site.register(Speech)
admin.site.register(MainCourse)
admin.site.register(Student)
admin.site.site_header = "Family and friends"
admin.site.site_title = "Family and friends"

from django.contrib import admin
from .models import Question

# Register your models here.
#Telling admin that Question objects have admin interface
admin.site.register(Question)
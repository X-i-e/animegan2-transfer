from django.contrib import admin
from .models import RawPic, ProcessedPic

# Register your models here.
admin.site.register(RawPic)
admin.site.register(ProcessedPic)

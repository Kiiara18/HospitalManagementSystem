from django.contrib import admin
from HospitalApp.models import Users,Products,Members,Message

# Register your models here.
admin.site.register(Users)
admin.site.register(Products)
admin.site.register(Members)
admin.site.register(Message)
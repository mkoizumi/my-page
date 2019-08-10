from django.contrib import admin
# importing our objects from models.py
from template_app.models import AccessRecord, Topic, Webpage


# Register your models here - only people who are working with website (ME!!)
# can access register
admin.site.register(AccessRecord)
admin.site.register(Topic)
admin.site.register(Webpage)

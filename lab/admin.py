from django.contrib import admin

# Register your models here.
from . models import Admission
admin.site.register(Admission)

from . models import Contact
admin.site.register(Contact)
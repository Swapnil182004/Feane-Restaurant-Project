from django.contrib import admin
from Base_App.models import *

# Register your models here.

admin.site.register(ItemList)       #this name on bracket() comming from func names on models.py
admin.site.register(Items)
admin.site.register(AboutUs)
admin.site.register(BookTable)
admin.site.register(Feedback)
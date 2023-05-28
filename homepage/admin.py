from django.contrib import admin
from .models import *

class chapterAdmin(admin.ModelAdmin):
    list_display = ['truyen','title','id']

admin.site.register(truyen)
admin.site.register(chapter,chapterAdmin)
admin.site.register(truyen_category)
admin.site.register(category)
admin.site.register(comment)
admin.site.register(favorate)
# Register your models here.



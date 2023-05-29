from django.contrib import admin
from .models import *

class chapterAdmin(admin.ModelAdmin):
    list_display = ['truyen','title','id']

class CommentInline(admin.StackedInline):
    model = comment

class PostAdmin(admin.ModelAdmin):
    list_display = ['id','truyen','user', 'content' ,'date_published']

admin.site.register(truyen)
admin.site.register(chapter,chapterAdmin)
admin.site.register(truyen_category)
admin.site.register(category)
admin.site.register(comment,PostAdmin)
admin.site.register(favorate)
# Register your models here.



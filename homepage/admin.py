from django.contrib import admin
from .models import *

class chapterAdmin(admin.ModelAdmin):
    list_display = ['truyen','title','id']    
    list_filter = ['truyen']
    search_fields = ['truyen']

class truyen_categoryrAdmin(admin.ModelAdmin):
    list_display = ['Truyen','category']  
    list_filter = ['category']
    search_fields = ['Truyen']

class CommentInline(admin.TabularInline):
    model = comment

class CommentAdmin(admin.ModelAdmin):
    list_display = ['truyen','content','user', 'date_published']
    list_filter = ['date_published']
    search_fields = ['truyen']

class favoAdmin(admin.ModelAdmin):
    list_display = ['truyen','user','id']
    search_fields = ['truyen']
    list_filter = ['truyen']

class cateAdmin(admin.ModelAdmin):
    list_display = ['title','content']
    search_fields = ['title']
    list_filter = ['title']

class truyenmAdmin(admin.ModelAdmin):
    list_display = ['title','author','date_published','view_count']
    list_filter = ['author']

    

admin.site.register(truyen,truyenmAdmin)
admin.site.register(chapter,chapterAdmin)
admin.site.register(truyen_category,truyen_categoryrAdmin)
admin.site.register(category,cateAdmin)
admin.site.register(comment,CommentAdmin)
admin.site.register(favorate,favoAdmin)
# Register your models here.



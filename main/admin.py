from django.contrib import admin
from .models import Notice

# admin.site.register(Notice)

@admin.register(Notice)
class NoticeAdmin(admin.ModelAdmin):
    list_display=['title','likeCount']
    list_display_links=['title','likeCount']
    
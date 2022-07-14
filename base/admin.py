from django.contrib import admin
from .models import Category,Tag,Post
# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id','name','slug')
admin.site.register(Category,CategoryAdmin)

class TagAdmin(admin.ModelAdmin):
    list_display = ('id','name','slug')
admin.site.register(Tag,TagAdmin)

class PostAdmin(admin.ModelAdmin):
    list_display = ('id','title','slug','feature')
admin.site.register(Post,PostAdmin)

admin.site.site_header  =  "Northernalliance Admin"  
admin.site.site_title  =  "Northernalliance News"
admin.site.index_title  =  "Northernalliance  Admin"
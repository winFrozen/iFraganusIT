from django.contrib import admin
from blog.models import Konsultatsiya, Teachers, About, Aboutus, Course, Categoriya, Pupils, Pupils2, Pupils3, Pupils4, \
    Pupils5, Teamtopbar, Itcourse, Kids, Ittopbar, News

# Register your models here.

admin.site.register(Konsultatsiya)
admin.site.register(Teachers)
admin.site.register(About)
admin.site.register(Aboutus)
admin.site.register(Course)
admin.site.register(Pupils)
admin.site.register(Pupils2)
admin.site.register(Pupils3)
admin.site.register(Pupils4)
admin.site.register(Pupils5)
admin.site.register(Categoriya)
admin.site.register(Teamtopbar)
admin.site.register(Ittopbar)
admin.site.register(News)

@admin.register(Itcourse)
class ItcourseAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ('name',)}

@admin.register(Kids)
class KidsAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ('name',)}
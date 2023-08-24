from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Home)
admin.site.register(Skill)
admin.site.register(TimeLine)
admin.site.register(Portfolio)

class LinksInline(admin.TabularInline):
    model = Links
    extra = 1

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    inlines = [LinksInline]

admin.site.register(SocialMedia)
admin.site.register(Message)
admin.site.register(Contact)



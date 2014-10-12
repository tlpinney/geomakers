from django.contrib import admin
from skyshaker.models import Image, Link, MakerSpace, Profile, Project, Tag, Video

class ProjectAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Link)
admin.site.register(MakerSpace)
admin.site.register(Profile)
admin.site.register(Project, ProjectAdmin)
admin.site.register(Tag)
admin.site.register(Video)
admin.site.register(Image)

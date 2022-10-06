from django.contrib import admin

from notes_app.my_web.models import Profile, Note


# admin.site.register(Profile)
# admin.site.register(Note)


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name',)
    list_filter = ('age',)
    search_fields = ('first_name', 'last_name',)




@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    list_display = ('id', 'title',)

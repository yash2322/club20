from django.contrib import admin
from .models import UpcomingEvents,SuccessfullEvents,SuccessfullEventsImages,Feedback,ContactSection
from django.contrib.auth.models import User
from django.contrib.auth.models import Group

# Register your models here.

# Register your models here.
@admin.register(UpcomingEvents)
class UpcomingEventsAdmin(admin.ModelAdmin):
    list_display = ['title', 'date']
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ['date']


class SuccessfullEventsImagesInline(admin.StackedInline):
    model = SuccessfullEventsImages


@admin.register(ContactSection)
class ContactSectionAdmin(admin.ModelAdmin):

    list_display = ['name', 'email','message']
    list_filter = ['date']
    readonly_fields = ('name',
                       'email',
                       'message')

    def has_add_permission(self, request):
        return False
    def has_delete_permission(self, request, obj=None):
        return True



@admin.register(SuccessfullEvents)
class SuccessfullEventsAdmin(admin.ModelAdmin):
    list_display = ['title', 'date']
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ['date']

    inlines = [SuccessfullEventsImagesInline]


@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ['firstname','lastname','feedType','message']
    readonly_fields = ('firstname','lastname','feedType','message')

    def has_add_permission(self, request):
        return False
    def has_delete_permission(self, request, obj=None):
        return True





admin.site.unregister(User)
admin.site.unregister(Group)

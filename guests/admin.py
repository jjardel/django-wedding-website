from django.contrib import admin
from .models import Guest, Party


class GuestInline(admin.TabularInline):
    model = Guest
    fields = ('first_name', 'last_name', 'is_attending', 'meal', 'is_child')
    readonly_fields = ('first_name', 'last_name')


class PartyAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'category', 'invitation_opened',
                    'is_invited', 'is_attending', 'preferred_transportation', 'party_email', 'comments')
    list_filter = ('type', 'category', 'is_invited', 'is_attending', 'invitation_opened', 'preferred_transportation')
    inlines = [GuestInline]


class GuestAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'party', 'is_attending', 'is_child', 'meal')
    list_filter = ('is_attending', 'is_child', 'meal', 'party__is_invited')


admin.site.register(Party, PartyAdmin)
admin.site.register(Guest, GuestAdmin)

from django.contrib import admin
from polls.models import Question, Choice
from django.contrib.admin import AdminSite

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]

    list_display = ('question_text','pub_date','was_published_recently')
    list_filter = ['pub_date']
    search_fields = ['question_text']


class MyAdminSite(AdminSite):
    site_header ='Poll Apps Administration'

admin_site = MyAdminSite(name='admin')
admin_site.register(Question, QuestionAdmin)
# Register your models here.
#admin.site.register(Choice)

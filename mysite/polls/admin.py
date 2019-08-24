from django.contrib import admin
from .models import Question, Choice
""""
to add choices directly to one question,removing,admin.site.register(choice)
"""
class ChoiceInline(admin.TabularInline):            #replace tabular by stack
    model = Choice
    extra = 1


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        ("LOL",               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
                ]
    inlines = [ChoiceInline]
    list_display = ('question_text', 'pub_date')
admin.site.register(Question, QuestionAdmin)



# Register your models here.

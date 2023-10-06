from django.contrib import admin
from .models import Participant, Test, Question, TestParticipant, Time

# Register your models here.

admin.site.register(Participant)
admin.site.register(Test)
admin.site.register(Question)
admin.site.register(TestParticipant)
admin.site.register(Time)

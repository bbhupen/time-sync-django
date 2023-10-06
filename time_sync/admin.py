from django.contrib import admin
from .models import Participant, Test, Questions, TestParticipants, Time

# Register your models here.

admin.site.register(Participant)
admin.site.register(Test)
admin.site.register(Questions)
admin.site.register(TestParticipants)
admin.site.register(Time)

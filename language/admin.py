from django.contrib import admin
from .forms import TransalationForm
from .models import Transalation


class YourModelAdmin(admin.ModelAdmin):
    def get_form(self, request, obj=None, **kwargs):
        return TransalationForm

admin.site.register(Transalation, YourModelAdmin)
from django import forms
from .models import Transalation
from django.conf import settings

class TransalationForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        ins = kwargs.get('instance', None)
        super(TransalationForm, self).__init__(*args, **kwargs)
        text = {}
        if ins:
            text = ins.text
        for i in (settings.LANGUAGES):
            field_name = 'article_title_(%s)' % (i[0],)
            self.base_fields[field_name] = forms.CharField(initial= text.get(i[0], ''))
            self.fields[field_name] = forms.CharField(initial= text.get(i[0], ''))

    def save(self, commit: bool = True) :
        instance = super(TransalationForm, self).save(commit=False)
        out = {}
        for i in (settings.LANGUAGES):
            field_name = 'article_title_(%s)' % (i[0],)
            extra_field = self.cleaned_data.get(field_name, None)
            out[i[0]] = extra_field
        instance.text = out
        if commit:
            instance.save()
        return instance

    class Meta:
        model = Transalation
        exclude = ['text']
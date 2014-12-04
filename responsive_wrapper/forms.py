from django import forms
from django.utils import six

from .conf import settings
from .models import ResponsiveWrapper


class ResponsiveWrapperForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(ResponsiveWrapperForm, self).__init__(*args, **kwargs)

        for name, config in six.iteritems(settings.RESPONSIVE_MEDIA_QUERIES):
            label = config.get('verbose_name', name.replace('_', ' ').title())
            help_text = config.get('help_text', '')
            self.fields[name] = forms.BooleanField(
                label=label, help_text=help_text, initial=True, required=False)

        if bool(self.instance.pk):
            self.initial.update(self.instance.media_queries)

    def save(self, commit=True):
        instance = super(ResponsiveWrapperForm, self).save(commit=False)
        instance.media_queries = self.cleaned_data
        if commit:
            instance.save()
        return instance

    class Meta:
        model = ResponsiveWrapper

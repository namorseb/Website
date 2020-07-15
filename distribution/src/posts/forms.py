from django import forms
from django.contrib.flatpages.models import FlatPage
from tinymce.widgets import TinyMCE

class MyForm(forms.ModelForm):
    ...
    content = forms.CharField(widget=TinyMCE(attrs={'cols': 80, 'rows': 30}))
    ...

    class Meta:
        model = MyForm

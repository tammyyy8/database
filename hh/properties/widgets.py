
from django import forms

class MultiFileInput(forms.ClearableFileInput):
    template_name = 'forms/widgets/multiple_input.html'

    def value_from_datadict(self, data, files, name):
        return files.getlist(name)

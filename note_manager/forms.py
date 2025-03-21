from django import forms

class AddNoteForm(forms.Form):
    title = forms.CharField(max_length=100)
    content = forms.CharField(required=False)
    
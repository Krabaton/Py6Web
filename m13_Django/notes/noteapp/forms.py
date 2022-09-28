from django.forms import ModelForm
from .models import Tag, Note


class TagForm(ModelForm):
    class Meta:
        model = Tag
        fields = ['name']


class NoteForm(ModelForm):
    class Meta:
        model = Note
        fields = ['name', 'description']
        exclude = ['tags']

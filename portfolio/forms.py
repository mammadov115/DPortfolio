from django import forms
from .models import Message

class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'YOUR NAME', 'required':''}),
            'email': forms.TextInput(attrs={'placeholder': 'YOUR EMAIL', 'required':''}),
            'subject': forms.TextInput(attrs={'placeholder': 'ENTER SUBJECT', 'required':''}),
            'text': forms.Textarea(attrs={'placeholder': "Message Here...", 'required':'', 'cols': 15, 'rows': 8})
        }
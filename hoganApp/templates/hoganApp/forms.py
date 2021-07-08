from django import forms
from hoganApp.models import Conversation, Message, Thought

class ConversationForm(forms.ModelForm):
    class Meta:
        model = Conversation
        fields = ("title","startdate",)   # NOTE: the trailing comma is required

class ConvoSearchForm(forms.ModelForm):
    class Meta:
        model = Conversation
        fields = ("title",)

class MessageSearchForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ("text",)

class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ("text",)   # NOTE: the trailing comma is required
        widgets = {'title': forms.HiddenInput()}

class ThoughtForm(forms.ModelForm):
    class Meta:
        model = Thought
        fields = ("text",)   # NOTE: the trailing comma is required
        widgets = {'title': forms.HiddenInput()}
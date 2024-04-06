from django import forms
from .models import Quest

class QuestForm(forms.ModelForm):
    class Meta:
        model = Quest
        fields = ['quest_name', 'description', 'pc_involved', 'is_completed', 'reward']
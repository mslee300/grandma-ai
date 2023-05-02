from django import forms
from grandmaai.models import Goal, Level, Email, Phone


class GoalForm(forms.ModelForm):
    class Meta:
        model = Goal  # 사용할 모델
        fields = ['content']  # GoalForm에서 사용할 Goal 모델의 속성

class LevelForm(forms.ModelForm):
    class Meta:
        model = Level  # 사용할 모델
        fields = ['level']  # LevelForm에서 사용할 Level 모델의 속성

class EmailForm(forms.ModelForm):
    class Meta:
        model = Email  # 사용할 모델
        fields = ['email']  # EmailForm에서 사용할 Email 모델의 속성

class PhoneForm(forms.ModelForm):
    class Meta:
        model = Phone  # 사용할 모델
        fields = ['phone']  # PhoneForm에서 사용할 Phone 모델의 속성
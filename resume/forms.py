from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(
        max_length=30,
        label='',
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Write your name here'
            }
        )
    )
    email = forms.EmailField(
        label='',
        widget=forms.EmailInput(
            attrs={
                'placeholder': 'Write your email here'
            }
        ))
    message = forms.CharField(
        max_length=300,
        label='',
        widget = forms.Textarea(
            attrs={
                'rows':4,
                'placeholder': 'Write your message here'}))

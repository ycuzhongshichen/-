from django import forms

from .model import Student

class StudentForm(forms.Form):
    def clean_qq(self):
        cleaned_data = self.cleaned_data['qq']
    if not cleaned_data.isdigit():
        raise forms.Validationerror('')
    return int(cleaned_data)

class Meta:
    model = Student
    fields = ('name','sex','profession','email','qq','phone')

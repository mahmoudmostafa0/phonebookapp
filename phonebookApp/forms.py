# forms.py
from django import forms
from .models import Contact, PhoneNumber

class PhoneNumberForm(forms.ModelForm):
    class Meta:
        model = PhoneNumber
        fields = ['phone_number']

class ContactForm(forms.ModelForm):
    phone_numbers = forms.CharField(widget=forms.Textarea, help_text='Enter phone numbers separated by commas')

    class Meta:
        model = Contact
        fields = ['name', 'email', 'address']

    def save(self, commit=True):
        contact = super().save(commit=False)
        if commit:
            contact.save()
        phone_numbers = self.cleaned_data['phone_numbers']
        phone_number_list = [num.strip() for num in phone_numbers.split(',')]
        for num in phone_number_list:
            phone_number, created = PhoneNumber.objects.get_or_create(phone_number=num)
            contact.phone_number.add(phone_number)
        return contact

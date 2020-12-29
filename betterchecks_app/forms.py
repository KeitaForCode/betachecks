from django import forms
from betterchecks_app.models import Enquiry,CourseEnquiry,Contacts
from django.forms import Textarea



class EnquiryForm(forms.ModelForm):
    class Meta:
        model = Enquiry
        fields = '__all__'
        widgets = {
            'message':Textarea(attrs={'cols': 50, 'rows': 4}),
        }

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contacts
        fields = '__all__'
        widgets = {
            'message':Textarea(attrs={'cols':50, 'rows':3}),
        }
        

class CourseEnquiryForm(forms.ModelForm):
    class Meta:
        model = CourseEnquiry
        fields = '__all__'
        widgets = {
            'interest':Textarea(attrs={'cols':50,'rows':4}),
        }


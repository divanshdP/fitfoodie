from django import forms
from crispy_forms.helper import FormHelper
from app.models import *

class Login(forms.Form):
    #helper=FormHelper()
    cust_email=forms.EmailField(label="Email")
    cust_password=forms.CharField(label="Password",widget=forms.PasswordInput)

    def _clean_form(self):
        return super()._clean_form()
          

class Signup(forms.Form):
    cust_name=forms.CharField(label="Name")
    cust_email=forms.EmailField(label="Email")
    cust_password=forms.CharField(label="Password",widget=forms.PasswordInput,min_length=5)
    cust_confirm_password=forms.CharField(label="Confirm Password",widget=forms.PasswordInput)
    cust_phone=forms.CharField(label="Contact Number")
    gender=(
        ("Male","Male"),
        ("Female","Female"),
    )
    cust_gender=forms.ChoiceField(label="Gender",widget=forms.RadioSelect,choices=gender)
    cust_address=forms.CharField(label="Delievery Address",widget=forms.Textarea(attrs={'rows':3,'cols':10}))

    def clean(self):
        cleaned_data = super(Signup, self).clean()
        
        cust_email = cleaned_data.get('cust_email')
        for x in Customer.objects.all():
            if x.cust_email == cust_email :
                raise forms.ValidationError('Customer with ' + str(cust_email) + ' already registered ! Please Register with other Email Address')

        cust_password = cleaned_data.get("cust_password")
        cust_confirm_password = cleaned_data.get("cust_confirm_password")

        if cust_password != cust_confirm_password:
            raise forms.ValidationError("Password and Confirm Password does not match")
            self.cust_confirm_password=''
    
        return cleaned_data

    def _clean_form(self):
        return super()._clean_form()
        

class Mail(forms.Form):
    email_from=forms.EmailField(label="Email Id")
    email_password=forms.CharField(label="Password",widget=forms.PasswordInput)
    email_subject=forms.CharField(label="Subject")
    email_message=forms.CharField(label="Message",widget=forms.Textarea(attrs={'rows':5,'cols':10}))

    def __init__(self, *args, **kwargs):
        super(Mail, self).__init__(*args, **kwargs)
        self.initial['email_subject'] = 'Feedback Mail'

from django import forms
from ecommerceapp.models import Contact


class ContactForm(forms.ModelForm):
    class Meta:
        model=Contact
        fields=['sno','name','email','description','phonenumber']
        
    # def save(self,commit=True):
    #     Contact=super(ContactForm,self).save(commit=False)
    #     Contact.name = self.cleaned_data['name']
    #     Contact.email = self.cleaned_data['email']
    #     Contact.decription = self.cleaned_data['decription']
    #     Contact.phonenumber = self.cleaned_data['phonenumber']
    #     if commit:
    #         Contact.save()
    #     else:
    #         return Contact
    # def save(self, *args, **kwargs):
    #     pass
    
        # widgets = {
        #     'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Full Name'}),
        #     'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email Address'}),
        #     'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'How Can I Help You?'}),
        #     'phonenumber': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Phone Number'}),
        # }
        # labels = {
        #     'name': 'Full Name',
        #     'email': 'Email Address',
        #     'description': 'How Can I Help You?',
        #     'phonenumber': 'Phone Number',
        # }

 
    
     
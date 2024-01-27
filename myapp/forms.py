from django import forms
from .models import Membernew

class MemberForm(forms.ModelForm):
   class Meta:
     model = Membernew
     fields = ['firstname','lastname','image','rollno','phoneno']
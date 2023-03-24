# from django import forms
from django.forms import ModelForm
from .models import MedicalRecord







class MedicalRecordForm(ModelForm):
    
	class Meta:
		model = MedicalRecord
		exclude = ['doctors_notes', 'test_and_procedures','date_of_diagnosis','medication','allergies', 'image', 'email', 'patient']
		# my_field = ModelForm.ChoiceField(choices=choices, validate_choice=False)
# from django import forms
# from .models import MedicalRecord

# class MedicalRecordFilterForm(forms.Form):
#     record_type = forms.ChoiceField(choices=[('', '---')] + list(MedicalRecord.objects.values_list('record_type', 'record_type').distinct()))

import random
from django.contrib.auth.models import User

from .models import Property, WorkGenM, BuildsecM, ElectsectionM, CivilsectionM, UserProfile

from django import forms
from .models import Contract

from django import forms
from .models import Property  # Ensure Property model is correctly imported

class PropertyForm(forms.ModelForm):
    PROPERTY_TYPE_CHOICES = [
        ('', 'Type of Property'),  # Placeholder option
        ('Residential', 'Residential'),
        ('Commercial', 'Commercial'),
        ('Industrial', 'Industrial'),
    ]

    property_no = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control text-left'}))
    coordinate = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control text-left'}))
    location = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control text-left'}))
    cost = forms.DecimalField(widget=forms.NumberInput(attrs={'class': 'form-control text-left'}))
    property_type = forms.ChoiceField(
        choices=PROPERTY_TYPE_CHOICES,
        widget=forms.Select(attrs={'class': 'form-control text-left'})
    )
    passport = forms.FileField(widget=forms.FileInput(attrs={'class': 'form-control text-left'}))

    class Meta:
        model = Property  # Link the form to the Property model
        fields = ['property_no', 'coordinate', 'location', 'cost', 'property_type', 'passport']

#
# class PropertyForm(forms.ModelForm):
#     class Meta:
#         model = Property  # Link the form to the Property model
#         fields = '__all__'
#
#         # Optional: Add custom widgets for styling
#     property_no = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
#     coordinate = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
#     location = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
#     cost = forms.DecimalField(widget=forms.NumberInput(attrs={'class': 'form-control'}))
#     property_type = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
#     passport = forms.FileField(widget=forms.FileInput(attrs={'class': 'form-control'}))
# class PropertyForm(forms.ModelForm):
#     class Meta:
#         model = Property
#         fields = ['property_no', 'coordinate', 'location', 'cost', 'property_type', 'passport']
#
# #
# class ContractForm(forms.ModelForm):
#     class Meta:
#         model = Contract
#         fields = '__all__'
#
#
# class ContractForm(forms.Form):
#     class Meta:
#         model = Contract  # Link the form to the Contract model
#         fields = '__all__'  # Use all fields from the model
#
#
#     contract_no = forms.CharField(label="Contract NO.", widget=forms.TextInput(attrs={'class': 'form-control'}))
#     title = forms.CharField(label="Title of Contract", widget=forms.TextInput(attrs={'class': 'form-control'}))
#     company_name = forms.CharField(label="Name of Company", widget=forms.TextInput(attrs={'class': 'form-control'}))
#     location = forms.CharField(label="Contract Location", widget=forms.TextInput(attrs={'class': 'form-control'}))
#
#     # File Upload Fields
#     contract_advert = forms.FileField(label="Contract Advert", widget=forms.FileInput(attrs={'class': 'form-control'}))
#     company_profile = forms.FileField(label="Company Profile", widget=forms.FileInput(attrs={'class': 'form-control'}))
#     contract_agreement = forms.FileField(label="Contract Agreement/G&gpc", widget=forms.FileInput(attrs={'class': 'form-control'}))
#     variations = forms.FileField(label="Variations", required=False, widget=forms.FileInput(attrs={'class': 'form-control'}))
#     applications = forms.FileField(label="Applications", widget=forms.FileInput(attrs={'class': 'form-control'}))
#     certificate_no_objection = forms.FileField(label="Certificate of No Objection", widget=forms.FileInput(attrs={'class': 'form-control'}))
#     award_certificate = forms.FileField(label="Award Certificate", widget=forms.FileInput(attrs={'class': 'form-control'}))
#     completion_certificate = forms.FileField(label="Completion Certificate", widget=forms.FileInput(attrs={'class': 'form-control'}))
#     drawing = forms.FileField(label="Drawing", widget=forms.FileInput(attrs={'class': 'form-control'}))
#     certificate_valuation = forms.FileField(label="Certificate of Valuation", widget=forms.FileInput(attrs={'class': 'form-control'}))
#     approvals = forms.FileField(label="Approvals", widget=forms.FileInput(attrs={'class': 'form-control'}))


  # Import your Contract model
#
# class ContractForm(forms.ModelForm):
#     class Meta:
#         model = Contract  # Connect the form to the Contract model
#         fields = '__all__'  # Use all fields from the model
#
#     contract_no = forms.CharField(label="Contract NO.", widget=forms.TextInput(attrs={'class': 'form-control'}))
#     title = forms.CharField(label="Title of Contract", widget=forms.TextInput(attrs={'class': 'form-control'}))
#     company_name = forms.CharField(label="Name of Company", widget=forms.TextInput(attrs={'class': 'form-control'}))
#     location = forms.CharField(label="Contract Location", widget=forms.TextInput(attrs={'class': 'form-control'}))
#
#     # File Upload Fields
#     contract_advert = forms.FileField(label="Contract Advert", widget=forms.FileInput(attrs={'class': 'form-control'}))
#     company_profile = forms.FileField(label="Company Profile", widget=forms.FileInput(attrs={'class': 'form-control'}))
#     contract_agreement = forms.FileField(label="Contract Agreement/G&gpc", widget=forms.FileInput(attrs={'class': 'form-control'}))
#     variations = forms.FileField(label="Variations", required=False, widget=forms.FileInput(attrs={'class': 'form-control'}))
#     applications = forms.FileField(label="Applications", widget=forms.FileInput(attrs={'class': 'form-control'}))
#     certificate_no_objection = forms.FileField(label="Certificate of No Objection", widget=forms.FileInput(attrs={'class': 'form-control'}))
#     award_certificate = forms.FileField(label="Award Certificate", widget=forms.FileInput(attrs={'class': 'form-control'}))
#     completion_certificate = forms.FileField(label="Completion Certificate", widget=forms.FileInput(attrs={'class': 'form-control'}))
#     drawing = forms.FileField(label="Drawing", widget=forms.FileInput(attrs={'class': 'form-control'}))
#     certificate_valuation = forms.FileField(label="Certificate of Valuation", widget=forms.FileInput(attrs={'class': 'form-control'}))
#     approvals = forms.FileField(label="Approvals", widget=forms.FileInput(attrs={'class': 'form-control'}))
#
#     def __init__(self, *args, **kwargs):
#         super(ContractForm, self).__init__(*args, **kwargs)
#         if not self.initial.get('contract_no'):
#             random_no = f"CNT-{random.randint(10000, 99999)}"
#             self.fields['contract_no'].initial = random_no



class ContractForm(forms.ModelForm):
    contract_no = forms.CharField(
        label="Contract NO.",
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    title = forms.CharField(
        label="Title of Contract",
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    company_name = forms.CharField(
        label="Name of Company",
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    location = forms.CharField(
        label="Contract Location",
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )

    # File Upload Fields
    contract_advert = forms.FileField(label="Contract Advert", widget=forms.FileInput(attrs={'class': 'form-control'}))
    company_profile = forms.FileField(label="Company Profile", widget=forms.FileInput(attrs={'class': 'form-control'}))
    contract_agreement = forms.FileField(label="Contract Agreement/G&gpc", widget=forms.FileInput(attrs={'class': 'form-control'}))
    variations = forms.FileField(label="Variations", required=False, widget=forms.FileInput(attrs={'class': 'form-control'}))
    applications = forms.FileField(label="Applications", widget=forms.FileInput(attrs={'class': 'form-control'}))
    certificate_no_objection = forms.FileField(label="Certificate of No Objection", widget=forms.FileInput(attrs={'class': 'form-control'}))
    award_certificate = forms.FileField(label="Award Certificate", widget=forms.FileInput(attrs={'class': 'form-control'}))
    completion_certificate = forms.FileField(label="Completion Certificate", widget=forms.FileInput(attrs={'class': 'form-control'}))
    drawing = forms.FileField(label="Drawing", widget=forms.FileInput(attrs={'class': 'form-control'}))
    certificate_valuation = forms.FileField(label="Certificate of Valuation", widget=forms.FileInput(attrs={'class': 'form-control'}))
    approvals = forms.FileField(label="Approvals", widget=forms.FileInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Contract
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(ContractForm, self).__init__(*args, **kwargs)
        if not self.initial.get('contract_no'):
            self.fields['contract_no'].initial = f"MGU/land/2025/{random.randint(10000, 99999)}"


class WorkGen(forms.ModelForm):
    class Meta:
        model = WorkGenM  # Connect the form to the Contract model
        fields = '__all__'  # Use all fields from the model

    contract_no = forms.CharField(label="Contract NO.", widget=forms.TextInput(attrs={'class': 'form-control'}))
    title = forms.CharField(label="Title of Contract", widget=forms.TextInput(attrs={'class': 'form-control'}))
    company_name = forms.CharField(label="Name of Company", widget=forms.TextInput(attrs={'class': 'form-control'}))
    location = forms.CharField(label="Contract Location", widget=forms.TextInput(attrs={'class': 'form-control'}))

    # File Upload Fields
    contract_advert = forms.FileField(label="Contract Advert", widget=forms.FileInput(attrs={'class': 'form-control'}))
    company_profile = forms.FileField(label="Company Profile", widget=forms.FileInput(attrs={'class': 'form-control'}))
    contract_agreement = forms.FileField(label="Contract Agreement/G&gpc", widget=forms.FileInput(attrs={'class': 'form-control'}))
    variations = forms.FileField(label="Variations", required=False, widget=forms.FileInput(attrs={'class': 'form-control'}))
    applications = forms.FileField(label="Applications", widget=forms.FileInput(attrs={'class': 'form-control'}))
    certificate_no_objection = forms.FileField(label="Certificate of No Objection", widget=forms.FileInput(attrs={'class': 'form-control'}))
    award_certificate = forms.FileField(label="Award Certificate", widget=forms.FileInput(attrs={'class': 'form-control'}))
    completion_certificate = forms.FileField(label="Completion Certificate", widget=forms.FileInput(attrs={'class': 'form-control'}))
    drawing = forms.FileField(label="Drawing", widget=forms.FileInput(attrs={'class': 'form-control'}))
    certificate_valuation = forms.FileField(label="Certificate of Valuation", widget=forms.FileInput(attrs={'class': 'form-control'}))
    approvals = forms.FileField(label="Approvals", widget=forms.FileInput(attrs={'class': 'form-control'}))

    class Meta:
        model = WorkGenM
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(WorkGen, self).__init__(*args, **kwargs)
        if not self.initial.get('contract_no'):
            self.fields['contract_no'].initial = f"MGU/WorkGenM/2025/{random.randint(10000, 99999)}"











class Buildsec(forms.ModelForm):
    # class Meta:
    #     model = BuildsecM  # Connect the form to the Contract model
    #     fields = '__all__'  # Use all fields from the model

    contract_no = forms.CharField(label="Contract NO.", widget=forms.TextInput(attrs={'class': 'form-control'}))
    title = forms.CharField(label="Title of Contract", widget=forms.TextInput(attrs={'class': 'form-control'}))
    company_name = forms.CharField(label="Name of Company", widget=forms.TextInput(attrs={'class': 'form-control'}))
    location = forms.CharField(label="Contract Location", widget=forms.TextInput(attrs={'class': 'form-control'}))

    # File Upload Fields
    contract_advert = forms.FileField(label="Contract Advert", widget=forms.FileInput(attrs={'class': 'form-control'}))
    company_profile = forms.FileField(label="Company Profile", widget=forms.FileInput(attrs={'class': 'form-control'}))
    contract_agreement = forms.FileField(label="Contract Agreement/G&gpc", widget=forms.FileInput(attrs={'class': 'form-control'}))
    variations = forms.FileField(label="Variations", required=False, widget=forms.FileInput(attrs={'class': 'form-control'}))
    applications = forms.FileField(label="Applications", widget=forms.FileInput(attrs={'class': 'form-control'}))
    certificate_no_objection = forms.FileField(label="Certificate of No Objection", widget=forms.FileInput(attrs={'class': 'form-control'}))
    award_certificate = forms.FileField(label="Award Certificate", widget=forms.FileInput(attrs={'class': 'form-control'}))
    completion_certificate = forms.FileField(label="Completion Certificate", widget=forms.FileInput(attrs={'class': 'form-control'}))
    drawing = forms.FileField(label="Drawing", widget=forms.FileInput(attrs={'class': 'form-control'}))
    certificate_valuation = forms.FileField(label="Certificate of Valuation", widget=forms.FileInput(attrs={'class': 'form-control'}))
    approvals = forms.FileField(label="Approvals", widget=forms.FileInput(attrs={'class': 'form-control'}))

    class Meta:
        model = BuildsecM
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(Buildsec, self).__init__(*args, **kwargs)
        if not self.initial.get('contract_no'):
            self.fields['contract_no'].initial = f"MGU/build/2025/{random.randint(10000, 99999)}"


class Electsection(forms.ModelForm):
    # class Meta:
    #     model = ElectsectionM  # Connect the form to the Contract model
    #     fields = '__all__'  # Use all fields from the model

    contract_no = forms.CharField(label="Contract NO.", widget=forms.TextInput(attrs={'class': 'form-control'}))
    title = forms.CharField(label="Title of Contract", widget=forms.TextInput(attrs={'class': 'form-control'}))
    company_name = forms.CharField(label="Name of Company", widget=forms.TextInput(attrs={'class': 'form-control'}))
    location = forms.CharField(label="Contract Location", widget=forms.TextInput(attrs={'class': 'form-control'}))

    # File Upload Fields
    contract_advert = forms.FileField(label="Contract Advert", widget=forms.FileInput(attrs={'class': 'form-control'}))
    company_profile = forms.FileField(label="Company Profile", widget=forms.FileInput(attrs={'class': 'form-control'}))
    contract_agreement = forms.FileField(label="Contract Agreement/G&gpc", widget=forms.FileInput(attrs={'class': 'form-control'}))
    variations = forms.FileField(label="Variations", required=False, widget=forms.FileInput(attrs={'class': 'form-control'}))
    applications = forms.FileField(label="Applications", widget=forms.FileInput(attrs={'class': 'form-control'}))
    certificate_no_objection = forms.FileField(label="Certificate of No Objection", widget=forms.FileInput(attrs={'class': 'form-control'}))
    award_certificate = forms.FileField(label="Award Certificate", widget=forms.FileInput(attrs={'class': 'form-control'}))
    completion_certificate = forms.FileField(label="Completion Certificate", widget=forms.FileInput(attrs={'class': 'form-control'}))
    drawing = forms.FileField(label="Drawing", widget=forms.FileInput(attrs={'class': 'form-control'}))
    certificate_valuation = forms.FileField(label="Certificate of Valuation", widget=forms.FileInput(attrs={'class': 'form-control'}))
    approvals = forms.FileField(label="Approvals", widget=forms.FileInput(attrs={'class': 'form-control'}))

    class Meta:
        model = ElectsectionM
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(Electsection, self).__init__(*args, **kwargs)
        if not self.initial.get('contract_no'):
            self.fields['contract_no'].initial = f"MGU/Electsection/2025/{random.randint(10000, 99999)}"


class Civilsection(forms.ModelForm):
    class Meta:
        model = CivilsectionM  # Connect the form to the Contract model
        fields = '__all__'  # Use all fields from the model

    contract_no = forms.CharField(label="Contract NO.", widget=forms.TextInput(attrs={'class': 'form-control'}))
    title = forms.CharField(label="Title of Contract", widget=forms.TextInput(attrs={'class': 'form-control'}))
    company_name = forms.CharField(label="Name of Company", widget=forms.TextInput(attrs={'class': 'form-control'}))
    location = forms.CharField(label="Contract Location", widget=forms.TextInput(attrs={'class': 'form-control'}))

    # File Upload Fields
    contract_advert = forms.FileField(label="Contract Advert", widget=forms.FileInput(attrs={'class': 'form-control'}))
    company_profile = forms.FileField(label="Company Profile", widget=forms.FileInput(attrs={'class': 'form-control'}))
    contract_agreement = forms.FileField(label="Contract Agreement/G&gpc", widget=forms.FileInput(attrs={'class': 'form-control'}))
    variations = forms.FileField(label="Variations", required=False, widget=forms.FileInput(attrs={'class': 'form-control'}))
    applications = forms.FileField(label="Applications", widget=forms.FileInput(attrs={'class': 'form-control'}))
    certificate_no_objection = forms.FileField(label="Certificate of No Objection", widget=forms.FileInput(attrs={'class': 'form-control'}))
    award_certificate = forms.FileField(label="Award Certificate", widget=forms.FileInput(attrs={'class': 'form-control'}))
    completion_certificate = forms.FileField(label="Completion Certificate", widget=forms.FileInput(attrs={'class': 'form-control'}))
    drawing = forms.FileField(label="Drawing", widget=forms.FileInput(attrs={'class': 'form-control'}))
    certificate_valuation = forms.FileField(label="Certificate of Valuation", widget=forms.FileInput(attrs={'class': 'form-control'}))
    approvals = forms.FileField(label="Approvals", widget=forms.FileInput(attrs={'class': 'form-control'}))

    class Meta:
        model = CivilsectionM
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(Civilsection, self).__init__(*args, **kwargs)
        if not self.initial.get('contract_no'):
            self.fields['contract_no'].initial = f"MGU/Civilsection/2025/{random.randint(10000, 99999)}"

# class UserForm(forms.ModelForm):
#     password = forms.CharField(widget=forms.PasswordInput)
#
#     class Meta:
#         model = User
#         fields = ['username', 'email', 'password']
#
# class UserProfileForm(forms.ModelForm):
#     class Meta:
#         model = UserProfile
#         fields = ['phone', 'address']
from django.contrib.auth.models import AbstractUser,UserManager
from django.db import models

# Create your models here.
from django.db import models

# class Property(models.Model):
#     property_no = models.CharField(max_length=50)
#     coordinate = models.CharField(max_length=100)
#     location = models.CharField(max_length=100)
#     cost = models.DecimalField(max_digits=15, decimal_places=2)
#     property_type = models.CharField(
#         max_length=20,
#         choices=[("Residential", "Residential"), ("Commercial", "Commercial"), ("Industrial", "Industrial")]
#     )
#     passport = models.ImageField(upload_to='property_passports/', blank=True, null=True)
#
#     def __str__(self):
#         return f"{self.property_no} - {self.property_type}"

class Property(models.Model):
    property_no = models.CharField(max_length=100)
    coordinate = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    property_type = models.CharField(max_length=255)
    passport = models.FileField(upload_to='properties/')

    def __str__(self):
        return f"{self.property_no} - {self.location}"



#
# class Contract(models.Model):
#     contract_no = models.CharField(max_length=100)
#     title = models.CharField(max_length=255)
#     company_name = models.CharField(max_length=255)
#     location = models.CharField(max_length=255)
#
#     contract_advert = models.FileField(upload_to='contracts/')
#     company_profile = models.FileField(upload_to='contracts/')
#     contract_agreement = models.FileField(upload_to='contracts/')
#     variations = models.FileField(upload_to='contracts/', blank=True, null=True)
#     applications = models.FileField(upload_to='contracts/')
#     certificate_no_objection = models.FileField(upload_to='contracts/')
#     award_certificate = models.FileField(upload_to='contracts/')
#     completion_certificate = models.FileField(upload_to='contracts/')
#     drawing = models.FileField(upload_to='contracts/')
#     certificate_valuation = models.FileField(upload_to='contracts/')
#     approvals = models.FileField(upload_to='contracts/')
#
#     def __str__(self):
#         return f"{self.contract_no} - {self.title}"




class Contract(models.Model):
    contract_no = models.CharField(max_length=100)
    title = models.CharField(max_length=255)
    company_name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)

    # File Upload Fields
    contract_advert = models.FileField(upload_to='contracts/')
    company_profile = models.FileField(upload_to='contracts/')
    contract_agreement = models.FileField(upload_to='contracts/')
    variations = models.FileField(upload_to='contracts/', blank=True, null=True)
    applications = models.FileField(upload_to='contracts/')
    certificate_no_objection = models.FileField(upload_to='contracts/')
    award_certificate = models.FileField(upload_to='contracts/')
    completion_certificate = models.FileField(upload_to='contracts/')
    drawing = models.FileField(upload_to='contracts/')
    certificate_valuation = models.FileField(upload_to='contracts/')
    approvals = models.FileField(upload_to='contracts/')

    def __str__(self):
        return f"{self.contract_no} - {self.title}"










class WorkGenM(models.Model):
    contract_no = models.CharField(max_length=100)
    title = models.CharField(max_length=255)
    company_name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)

    # File Upload Fields
    contract_advert = models.FileField(upload_to='contracts/')
    company_profile = models.FileField(upload_to='contracts/')
    contract_agreement = models.FileField(upload_to='contracts/')
    variations = models.FileField(upload_to='contracts/', blank=True, null=True)
    applications = models.FileField(upload_to='contracts/')
    certificate_no_objection = models.FileField(upload_to='contracts/')
    award_certificate = models.FileField(upload_to='contracts/')
    completion_certificate = models.FileField(upload_to='contracts/')
    drawing = models.FileField(upload_to='contracts/')
    certificate_valuation = models.FileField(upload_to='contracts/')
    approvals = models.FileField(upload_to='contracts/')

    def __str__(self):
        return f"{self.contract_no} - {self.title}"








class BuildsecM(models.Model):
    contract_no = models.CharField(max_length=100)
    title = models.CharField(max_length=255)
    company_name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)

    # File Upload Fields
    contract_advert = models.FileField(upload_to='contracts/')
    company_profile = models.FileField(upload_to='contracts/')
    contract_agreement = models.FileField(upload_to='contracts/')
    variations = models.FileField(upload_to='contracts/', blank=True, null=True)
    applications = models.FileField(upload_to='contracts/')
    certificate_no_objection = models.FileField(upload_to='contracts/')
    award_certificate = models.FileField(upload_to='contracts/')
    completion_certificate = models.FileField(upload_to='contracts/')
    drawing = models.FileField(upload_to='contracts/')
    certificate_valuation = models.FileField(upload_to='contracts/')
    approvals = models.FileField(upload_to='contracts/')

    def __str__(self):
        return f"{self.contract_no} - {self.title}"





class ElectsectionM(models.Model):
    contract_no = models.CharField(max_length=100)
    title = models.CharField(max_length=255)
    company_name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)

    # File Upload Fields
    contract_advert = models.FileField(upload_to='contracts/')
    company_profile = models.FileField(upload_to='contracts/')
    contract_agreement = models.FileField(upload_to='contracts/')
    variations = models.FileField(upload_to='contracts/', blank=True, null=True)
    applications = models.FileField(upload_to='contracts/')
    certificate_no_objection = models.FileField(upload_to='contracts/')
    award_certificate = models.FileField(upload_to='contracts/')
    completion_certificate = models.FileField(upload_to='contracts/')
    drawing = models.FileField(upload_to='contracts/')
    certificate_valuation = models.FileField(upload_to='contracts/')
    approvals = models.FileField(upload_to='contracts/')

    def __str__(self):
        return f"{self.contract_no} - {self.title}"





class CivilsectionM(models.Model):
    contract_no = models.CharField(max_length=100)
    title = models.CharField(max_length=255)
    company_name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)

    # File Upload Fields
    contract_advert = models.FileField(upload_to='contracts/')
    company_profile = models.FileField(upload_to='contracts/')
    contract_agreement = models.FileField(upload_to='contracts/')
    variations = models.FileField(upload_to='contracts/', blank=True, null=True)
    applications = models.FileField(upload_to='contracts/')
    certificate_no_objection = models.FileField(upload_to='contracts/')
    award_certificate = models.FileField(upload_to='contracts/')
    completion_certificate = models.FileField(upload_to='contracts/')
    drawing = models.FileField(upload_to='contracts/')
    certificate_valuation = models.FileField(upload_to='contracts/')
    approvals = models.FileField(upload_to='contracts/')

    def __str__(self):
        return f"{self.contract_no} - {self.title}"



class UserProfile(AbstractUser):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    REQUIRED_FIELDS = ["email"]

    objects = UserManager()

# class UserProfile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     phone = models.CharField(max_length=20)
#     address = models.TextField(blank=True, null=True)
#
#     def __str__(self):
#         return self.user.username
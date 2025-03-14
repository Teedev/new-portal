from django.urls import path

from . import views
from .forms import WorkGen
from .views import login_view, listReg, property_form, upload_contract, lands_section_view, success_view, success_view1, \
  upload_contractBuildsec, upload_contractWorkGen, upload_contractElectsection, upload_contractCivilsection, register

urlpatterns = [
  #leave the login as the root URl
  path("", login_view, name="login"),
  
  path("listReg/", listReg, name="listReg"),
  path("property-form/", property_form, name="property_form"),
  path('upload/', upload_contract, name='upload_contract'),
  path('lands_section_view/', lands_section_view, name='lands_section_view'),
  path("success/", success_view, name="success"),
  path("success1/", success_view1, name="success1"),
  path("register/", register, name="register"),



  path('WorkGen/', upload_contractWorkGen, name='upload_contractWorkGen'),
  path("upload_contractBuildsec/", upload_contractBuildsec, name="upload_contractBuildsec"),
  path("upload_contractElectsection/", upload_contractElectsection, name="upload_contractElectsection"),

  path('WorkGen/', upload_contractCivilsection, name='upload_contractCivilsection'),

]